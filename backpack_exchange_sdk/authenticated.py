import base64
import json
import time
import requests
from cryptography.hazmat.primitives.asymmetric import ed25519
from requests.exceptions import JSONDecodeError
from typing import List


class AuthenticationClient:
    base_url = 'https://api.backpack.exchange/'
    private_key_obj: ed25519.Ed25519PrivateKey

    def __init__(self, public_key: str, secret_key: str, window: int = 5000):
        self.key = public_key
        self.private_key_obj = ed25519.Ed25519PrivateKey.from_private_bytes(
            base64.b64decode(secret_key)
        )
        self.window = window

    def _send_request(self, method, endpoint, action, params=None):
        """
        Send authenticated request to API endpoint.
        """
        url = f'{self.base_url}{endpoint}'
        ts = int(time.time() * 1e3)
        headers = self._generate_signature(action, ts, params)

        try:
            if method == 'GET':
                response = requests.get(url, headers=headers, params=params)
            elif method == 'DELETE':
                response = requests.delete(
                    url, headers=headers, data=json.dumps(params))
            else:
                response = requests.post(
                    url, headers=headers, data=json.dumps(params))

            if 200 <= response.status_code < 300:
                if response.status_code == 204:
                    return None
                try:
                    return response.json()
                except ValueError:
                    return response.text
            else:
                try:
                    error = response.json()
                    raise Exception(
                        f"API Error: {error.get('code')} - {error.get('message')}")
                except ValueError:
                    raise Exception(
                        f"HTTP Error {response.status_code}: {response.text}")

        except requests.exceptions.RequestException as e:
            raise Exception(f"Request failed: {str(e)}")

    def _generate_signature(self, action: str, timestamp: int, params=None):
        if params:
            if 'postOnly' in params:
                params = params.copy()
                params['postOnly'] = str(params['postOnly']).lower()
            param_str = "&" + \
                "&".join(f"{k}={v}" for k, v in sorted(params.items()))
        else:
            param_str = ''
        if not param_str:
            param_str = ''
        sign_str = f"instruction={action}{param_str}&timestamp={timestamp}&window={self.window}"
        signature = base64.b64encode(
            self.private_key_obj.sign(sign_str.encode())).decode()
        return {
            "X-API-Key": self.key,
            "X-Signature": signature,
            "X-Timestamp": str(timestamp),
            "X-Window": str(self.window),
            "Content-Type": "application/json; charset=utf-8",
        }

    # ================================================================
    # Account - Account settings.
    # ================================================================
    def get_account(self):
        """
        Retrieves account settings.
        """
        return self._send_request('GET', 'api/v1/account', 'accountQuery')

    def update_account(self, autoBorrowSettlements: bool = None,
                       autoLend: bool = None,
                       autoRealizePnl: bool = None,
                       autoRepayBorrows: bool = None,
                       leverageLimit: str = None) -> None:
        """
        Update account settings.
        """
        data = {}
        if autoBorrowSettlements is not None:
            data['autoBorrowSettlements'] = autoBorrowSettlements
        if autoLend is not None:
            data['autoLend'] = autoLend
        if autoRealizePnl is not None:
            data['autoRealizePnl'] = autoRealizePnl
        if autoRepayBorrows is not None:
            data['autoRepayBorrows'] = autoRepayBorrows
        if leverageLimit is not None:
            data['leverageLimit'] = leverageLimit

        self._send_request(
            'PATCH', 'api/v1/account', 'accountUpdate', data)

    # ================================================================
    # Borrow Lend - Borrowing and lending.
    # ================================================================
    def get_borrow_lend_positions(self):
        """
        Retrieves all the open borrow lending positions for the account.
        """
        return self._send_request(
            'GET', 'api/v1/borrow-lend/positions', 'borrowLendPositionQuery')

    def execute_borrow_lend(self, quantity: str, side: str, symbol: str) -> None:
        """
        Execute a borrow or lend operation.
        """
        data = {
            'quantity': quantity,
            'side': side,
            'symbol': symbol
        }

        self._send_request('POST', 'api/v1/borrow-lend',
                           'borrowLendExecute', data)

    # ================================================================
    # Capital - Capital management.
    # ================================================================
    def get_balances(self):
        """
        Retrieves account balances and the state of the balances (locked or available).
        Locked assets are those that are currently in an open order.
        """
        return self._send_request(
            'GET', 'api/v1/capital', 'balanceQuery')

    def get_collateral(self, subAccountId: int = None):
        """
        Retrieves collateral information for an account.
        """
        params = {}
        if subAccountId is not None:
            params['subaccountId'] = subAccountId
        return self._send_request(
            'GET', 'api/v1/capital/collateral', 'collateralQuery', params)

    def get_deposits(self, fromTimestamp: int = None, toTimestamp: int = None, limit: int = 100, offset: int = 0):
        """
        Retrieves deposit history.
        """
        params = {'limit': limit, 'offset': offset}
        if fromTimestamp:
            params['from'] = fromTimestamp
        if toTimestamp:
            params['to'] = toTimestamp
        return self._send_request(
            'GET', 'wapi/v1/capital/deposits', 'depositQueryAll', params)

    def get_deposit_address(self, blockchain_name: str):
        """
        Retrieves the user specific deposit address if the user were to deposit on the specified blockchain.
        """
        params = {'blockchain': blockchain_name}
        return self._send_request(
            'GET', 'wapi/v1/capital/deposit/address', 'depositAddressQuery', params)

    def get_withdrawals(self, fromTimestamp: int = None, toTimestamp: int = None, limit: int = 100, offset: int = 0):
        """
        Retrieves withdrawal history.
        """
        params = {'limit': limit, 'offset': offset}
        if fromTimestamp:
            params['from'] = fromTimestamp
        if toTimestamp:
            params['to'] = toTimestamp
        return self._send_request(
            'GET', 'wapi/v1/capital/withdrawals', 'withdrawalQueryAll', params)

    def request_withdrawal(self, address: str,
                           blockchain: str,
                           quantity: str,
                           symbol: str,
                           client_id: str = None,
                           two_factor_token: str = None,
                           auto_borrow: bool = None,
                           auto_lend_redeem: bool = None):
        """
        Requests a withdrawal from the exchange.
        
        The twoFactorToken field is required if the withdrawal address is not an address that is configured in
        the address book to not require 2FA.
        """
        data = {
            'address': address,
            'blockchain': blockchain,
            'quantity': quantity,
            'symbol': symbol,
        }
        if client_id:
            data['clientId'] = client_id
        if two_factor_token:
            data['twoFactorToken'] = two_factor_token
        if auto_borrow is not None:
            data['autoBorrow'] = auto_borrow
        if auto_lend_redeem is not None:
            data['autoLendRedeem'] = auto_lend_redeem

        return self._send_request(
            'POST', 'wapi/v1/capital/withdrawals', 'withdraw', data)

    # ================================================================
    # Futures - Futures data.
    # ================================================================
    def get_open_positions(self):
        """
        Retrieves account position summary.
        """
        return self._send_request(
            'GET', 'api/v1/futures/positions', 'positionQuery')

    # ================================================================
    # History - Historical account data.
    # ================================================================
    def get_borrow_history(self, type: str = None,
                           sources: str = None,
                           positionId: str = None,
                           symbol: str = None,
                           limit: int = 100,
                           offset: int = 0):
        """
        History of borrow and lend operations for the account.
        """
        params = {'limit': limit, 'offset': offset}
        if type:
            params['type'] = type
        if sources:
            params['sources'] = sources
        if positionId:
            params['positionId'] = positionId
        if symbol:
            params['symbol'] = symbol
        return self._send_request(
            'GET', 'wapi/v1/history/borrowLend', 'borrowHistoryQueryAll', params)

    def get_interest_history(self, symbol: str = None,
                             positionId: str = None,
                             limit: int = 100,
                             offset: int = 0,
                             sources: str = None):
        """
        History of the interest payments for borrows and lends for the account.
        """
        params = {'limit': limit, 'offset': offset}
        if symbol:
            params['symbol'] = symbol
        if positionId:
            params['positionId'] = positionId
        if sources:
            params['sources'] = sources
        return self._send_request(
            'GET', 'wapi/v1/history/interest', 'interestHistoryQueryAll', params)

    def get_borrow_position_history(self, symbol: str = None,
                                    side: str = None,
                                    state: str = None,
                                    limit: int = 100,
                                    offset: int = 0):
        """
        History of borrow and lend positions for the account.
        """
        params = {'limit': limit, 'offset': offset}
        if symbol:
            params['symbol'] = symbol
        if side:
            params['side'] = side
        if state:
            params['state'] = state
        return self._send_request(
            'GET', 'wapi/v1/history/borrowLend/positions', 'borrowPositionHistoryQueryAll', params)

    def get_fill_history(self, orderId: str = None,
                         fromTimestamp: int = None,
                         toTimestamp: int = None,
                         symbol: str = None,
                         limit: int = 100,
                         offset: int = 0,
                         fillType: str = None):
        """
        Retrieves historical fills, with optional filtering for a specific order or symbol.
        """
        params = {'limit': limit, 'offset': offset}
        if orderId:
            params['orderId'] = orderId
        if fromTimestamp:
            params['from'] = fromTimestamp
        if toTimestamp:
            params['to'] = toTimestamp
        if symbol:
            params['symbol'] = symbol
        if fillType:
            params['fillType'] = fillType
        return self._send_request(
            'GET', 'wapi/v1/history/fills', 'fillHistoryQueryAll', params)

    def get_funding_payments(self, subaccountId: int = None, symbol: str = None, limit: int = 100, offset: int = 0):
        """
        Users funding payment history for futures.
        """
        params = {'limit': limit, 'offset': offset}
        if subaccountId:
            params['subaccountId'] = subaccountId
        if symbol:
            params['symbol'] = symbol
        return self._send_request(
            'GET', 'wapi/v1/history/funding', 'fundingHistoryQueryAll', params)

    def get_order_history(self, orderId: str = None, symbol: str = None, limit: int = 100, offset: int = 0):
        """
        Retrieves the order history for the user. This includes orders that have been filled and are no longer on
        the book. It may include orders that are on the book, but the /orders endpoint contains more up-to date data.
        """
        params = {'limit': limit, 'offset': offset}
        if symbol:
            params['symbol'] = symbol
        if orderId:
            params['orderId'] = orderId
        return self._send_request(
            'GET', 'wapi/v1/history/orders', 'orderHistoryQueryAll', params)

    def get_pnl_history(self, subaccountId: int = None, symbol: str = None, limit: int = 100, offset: int = 0):
        """
        History of profit and loss realization for an account.
        """
        params = {'limit': limit, 'offset': offset}
        if subaccountId:
            params['subaccountId'] = subaccountId
        if symbol:
            params['symbol'] = symbol
        return self._send_request(
            'GET', 'wapi/v1/history/pnl', 'pnlHistoryQueryAll', params)

    def get_settlement_history(self, limit: int = 100, offset: int = 0, source: str = None):
        """
        History of settlement operations for the account.
        """
        params = {'limit': limit, 'offset': offset}
        if source:
            params['source'] = source
        return self._send_request(
            'GET', 'wapi/v1/history/settlement', 'settlementHistoryQueryAll', params)

    # ================================================================
    # Order - Order management.
    # ================================================================

    def get_users_open_orders(self, symbol: str, clientId: int = None, orderId: str = None):
        """
        Retrieves an open order from the order book. This only returns the order if it is resting on the order book 
        (i.e. has not been completely filled, expired, or cancelled).
        
        One of orderId or clientId must be specified. If both are specified then the request will be rejected.
        """
        params = {'symbol': symbol}
        if clientId:
            params['clientId'] = clientId
        if orderId:
            params['orderId'] = orderId
        return self._send_request(
            'GET', 'api/v1/order', 'orderQuery', params)

    def execute_order(self, orderType: str, side: str, symbol: str,
                      postOnly: bool = False,
                      clientId: int = None,
                      price: str = None,
                      quantity: str = None,
                      timeInForce: str = None,
                      quoteQuantity: str = None,
                      selfTradePrevention: str = None,
                      triggerPrice: str = None,
                      reduceOnly: bool = None,
                      autoBorrow: bool = None,
                      autoBorrowRepay: bool = None,
                      autoLend: bool = None,
                      autoLendRedeem: bool = None):
        """
        Executes an order on the order book. If the order is not immediately filled,
        it will be placed on the order book.
        """
        data = {
            'orderType': orderType,
            'symbol': symbol,
            'side': side,
        }
        if orderType == 'Limit':
            data['price'] = price
            data['quantity'] = quantity
            if timeInForce:
                data['timeInForce'] = timeInForce
            else:
                data['postOnly'] = postOnly
        if orderType == 'Market':
            if quantity:
                data['quantity'] = quantity
            elif quoteQuantity:
                data['quoteQuantity'] = quoteQuantity
        if clientId:
            data['clientId'] = clientId
        if selfTradePrevention:
            data['selfTradePrevention'] = selfTradePrevention
        if triggerPrice:
            data['triggerPrice'] = triggerPrice
        if reduceOnly is not None:
            data['reduceOnly'] = reduceOnly
        if autoBorrow is not None:
            data['autoBorrow'] = autoBorrow
        if autoBorrowRepay is not None:
            data['autoBorrowRepay'] = autoBorrowRepay
        if autoLend is not None:
            data['autoLend'] = autoLend
        if autoLendRedeem is not None:
            data['autoLendRedeem'] = autoLendRedeem

        return self._send_request(
            'POST', 'api/v1/order', 'orderExecute', data)

    def cancel_open_order(self, symbol: str, clientId: int = None, orderId: str = None):
        """
        Cancels an open order from the order book.

        One of orderId or clientId must be specified. If both are specified then the request will be rejected.
        """
        data = {'symbol': symbol}
        if clientId:
            data['clientId'] = clientId
        if orderId:
            data['orderId'] = orderId
        return self._send_request(
            'DELETE', 'api/v1/order', 'orderCancel', data)

    def get_open_orders(self, symbol: str = None):
        """
        Retrieves all open orders. If a symbol is provided, only open orders for that market will be returned, otherwise
        all open orders are returned.
        """
        params = {}
        if symbol:
            params['symbol'] = symbol
        return self._send_request(
            'GET', 'api/v1/orders', 'orderQueryAll', params)

    def cancel_open_orders(self, symbol: str):
        """
        Cancels all open orders on the specified market.
        """
        params = {'symbol': symbol}
        return self._send_request(
            'DELETE', 'api/v1/orders', 'orderCancelAll', params)
