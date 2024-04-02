import base64
import json
import time
import requests
from cryptography.hazmat.primitives.asymmetric import ed25519
from requests.exceptions import JSONDecodeError


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
        url = f'{self.base_url}{endpoint}'
        ts = int(time.time() * 1e3)
        headers = self._generate_signature(action, ts, params)
        if method == 'GET':
            response = requests.get(url, headers=headers, params=params)
        elif method == 'DELETE':
            response = requests.delete(
                url, headers=headers, data=json.dumps(params))
        else:
            response = requests.post(
                url, headers=headers, data=json.dumps(params))
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.text}")
        try:
            data: dict = response.json()
            return data
        except JSONDecodeError:
            text: str = response.text
            return text

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
    # Capital - Capital management.
    # ================================================================
    def get_balances(self):
        """
        Retrieves account balances and the state of the balances (locked or available).
        Locked assets are those that are currently in an open order.
        """
        return self._send_request('GET', 'api/v1/capital', 'balanceQuery')

    def get_deposits(self, limit: int = 100, offset: int = 0):
        """
        Retrieves deposit history.
        """
        params = {'limit': limit, 'offset': offset}
        return self._send_request('GET', 'wapi/v1/capital/deposits', 'depositQueryAll', params)

    def get_deposit_address(self, blockchain_name: str):
        """
        Retrieves the user specific deposit address if the user were to deposit on the specified blockchain.
        """
        params = {'blockchain': blockchain_name}
        return self._send_request('GET', 'wapi/v1/capital/deposit/address', 'depositAddressQuery', params)

    def get_withdrawals(self, limit: int = 100, offset: int = 0):
        """
        Retrieves withdrawal history.
        """
        params = {'limit': limit, 'offset': offset}
        return self._send_request('GET', 'wapi/v1/capital/withdrawals', 'withdrawalQueryAll', params)

    def request_withdrawal(self, address: str,
                           blockchain: str,
                           quantity: str,
                           symbol: str,
                           client_id: str = None,
                           two_factor_token: str = None):
        """
        The twoFactorToken field is required if the withdrawal address is not an address that is configured in
        the address book to not require 2FA.

        The 2FA verification is currently experiencing errors. Please refrain from using 2FA for withdrawals
        at the moment.
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
        return self._send_request('POST', 'wapi/v1/capital/withdrawals', 'withdraw', data)

    # ================================================================
    # History - Historical account data.
    # ================================================================
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
        return self._send_request('GET', 'wapi/v1/history/orders', 'orderHistoryQueryAll', params)

    def get_fill_history(self, orderId: str = None, symbol: str = None, fromTimestamp: int = False, toTimestamp: int = False, limit: int = 100, offset: int = 0):
        """
        Retrieves historical fills, with optional filtering for a specific order or symbol.
        """
        params = {'limit': limit, 'offset': offset}
        if symbol:
            params['symbol'] = symbol
        if orderId:
            params['orderId'] = orderId
        if fromTimestamp:
            params['from'] = fromTimestamp
        if toTimestamp:
            params['to'] = toTimestamp
        return self._send_request('GET', 'wapi/v1/history/fills', 'fillHistoryQueryAll', params)
    # ================================================================
    # Order - Order management.
    # ================================================================

    def get_users_open_orders(self, symbol: str, clientId: int = False, orderId: str = None):
        """
        Retrieves an open order from the order book. This only returns the order if it is resting on the order book
        (i.e. has not been completely filled, expired, or cancelled).
        """
        params = {'symbol': symbol}
        if clientId:
            params['clientId'] = clientId
        if orderId:
            params['orderId'] = orderId
        return self._send_request('GET', 'api/v1/order', 'orderQuery', params)

    def execute_order(self, orderType: str, side: str, symbol: str, postOnly: bool = False, clientId: int = False,
                      price: str = None, quantity: str = None, timeInForce: str = None, quoteQuantity: str = None,
                      selfTradePrevention: str = None,  triggerPrice: str = None):
        """
        Executes an order on the order book. If the order is not immediately filled,
        it will be placed on the order book.
        Now only support Limit order.
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
        return self._send_request('POST', 'api/v1/order', 'orderExecute', data)

    def cancel_open_order(self, symbol: str, clientId: int = False, orderId: str = None):
        """
        Cancels an open order from the order book.

        One of orderId or clientId must be specified. If both are specified, then orderId takes precedence.
        """
        data = {'symbol': symbol}
        if clientId:
            data['clientId'] = clientId
        if orderId:
            data['orderId'] = orderId
        return self._send_request('DELETE', 'api/v1/order', 'orderCancel', data)

    def get_open_orders(self, symbol: str = None):
        """
        Retrieves all open orders. If a symbol is provided, only open orders for that market will be returned, otherwise
         all open orders are returned.
        """
        params = {}
        if symbol:
            params['symbol'] = symbol
        return self._send_request('GET', 'api/v1/orders', 'orderQueryAll', params)

    def cancel_open_orders(self, symbol: str):
        """
        Cancels all open orders on the specified market.
        """
        params = {'symbol': symbol}
        return self._send_request('DELETE', 'api/v1/orders', 'orderCancelAll', params)
