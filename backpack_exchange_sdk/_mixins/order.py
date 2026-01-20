"""
Order operations mixin for AuthenticationClient.
"""

from typing import Any, Dict, List, Optional, Union

from backpack_exchange_sdk.enums import (
    CancelOrderType,
    MarketType,
    OrderType,
    SelfTradePrevention,
    Side,
    TimeInForce,
)


class OrderMixin:
    """Mixin providing order-related operations."""

    def get_users_open_orders(
        self,
        symbol: str,
        clientId: Optional[int] = None,
        orderId: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Retrieves an open order from the order book.

        This only returns the order if it is resting on the order book.
        One of orderId or clientId must be specified.

        Args:
            symbol: Market symbol.
            clientId: Client-provided order ID.
            orderId: Exchange order ID.

        Returns:
            Order information.
        """
        params = {"symbol": symbol}
        if clientId:
            params["clientId"] = clientId
        if orderId:
            params["orderId"] = orderId
        return self._send_request("GET", "api/v1/order", "orderQuery", params)

    def execute_order(
        self,
        orderType: Union[OrderType, str],
        side: Union[Side, str],
        symbol: str,
        postOnly: bool = False,
        clientId: Optional[int] = None,
        brokerId: Optional[int] = None,
        price: Optional[str] = None,
        quantity: Optional[str] = None,
        timeInForce: Optional[Union[TimeInForce, str]] = None,
        quoteQuantity: Optional[str] = None,
        selfTradePrevention: Optional[Union[SelfTradePrevention, str]] = None,
        triggerPrice: Optional[str] = None,
        triggerBy: Optional[str] = None,
        reduceOnly: Optional[bool] = None,
        autoBorrow: Optional[bool] = None,
        autoBorrowRepay: Optional[bool] = None,
        autoLend: Optional[bool] = None,
        autoLendRedeem: Optional[bool] = None,
        stopLossTriggerPrice: Optional[str] = None,
        stopLossTriggerBy: Optional[str] = None,
        stopLossLimitPrice: Optional[str] = None,
        takeProfitTriggerPrice: Optional[str] = None,
        takeProfitTriggerBy: Optional[str] = None,
        takeProfitLimitPrice: Optional[str] = None,
        triggerQuantity: Optional[str] = None,
        slippageTolerance: Optional[str] = None,
        slippageToleranceType: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Executes an order on the order book.

        Args:
            orderType: Order type (Market or Limit).
            side: Order side (Bid or Ask).
            symbol: Market symbol.
            postOnly: Only post liquidity, do not take.
            clientId: Custom order ID.
            brokerId: Optional broker ID.
            price: Limit order price.
            quantity: Order quantity.
            timeInForce: How long the order is valid (GTC, IOC, FOK).
            quoteQuantity: Quote asset quantity for market orders.
            selfTradePrevention: Self-trade prevention mode.
            triggerPrice: Trigger price for conditional orders.
            triggerBy: Trigger by source.
            reduceOnly: Order can only reduce position (futures).
            autoBorrow: Enable auto borrow (spot margin).
            autoBorrowRepay: Enable auto borrow repay (spot margin).
            autoLend: Enable auto lend (spot margin).
            autoLendRedeem: Enable auto lend redeem (spot margin).
            stopLossTriggerPrice: Stop loss trigger price.
            stopLossTriggerBy: Stop loss trigger by source.
            stopLossLimitPrice: Stop loss limit price.
            takeProfitTriggerPrice: Take profit trigger price.
            takeProfitTriggerBy: Take profit trigger by source.
            takeProfitLimitPrice: Take profit limit price.
            triggerQuantity: Trigger quantity for conditional orders.
            slippageTolerance: Maximum slippage tolerance.
            slippageToleranceType: Slippage tolerance type.

        Returns:
            Order execution response.
        """
        data = {
            "orderType": orderType.value if isinstance(orderType, OrderType) else orderType,
            "symbol": symbol,
            "side": side.value if isinstance(side, Side) else side,
        }

        if orderType == OrderType.LIMIT or orderType == "Limit":
            data["price"] = price
            data["quantity"] = quantity
            if timeInForce:
                data["timeInForce"] = (
                    timeInForce.value if isinstance(timeInForce, TimeInForce) else timeInForce
                )
            else:
                data["postOnly"] = postOnly

        if orderType == OrderType.MARKET or orderType == "Market":
            if quantity:
                data["quantity"] = quantity
            elif quoteQuantity:
                data["quoteQuantity"] = quoteQuantity

        if clientId:
            data["clientId"] = clientId
        if brokerId is not None:
            data["brokerId"] = brokerId

        if selfTradePrevention:
            data["selfTradePrevention"] = (
                selfTradePrevention.value
                if isinstance(selfTradePrevention, SelfTradePrevention)
                else selfTradePrevention
            )

        if triggerPrice:
            data["triggerPrice"] = triggerPrice
        if triggerBy:
            data["triggerBy"] = triggerBy

        if reduceOnly is not None:
            data["reduceOnly"] = reduceOnly

        if autoBorrow is not None:
            data["autoBorrow"] = autoBorrow

        if autoBorrowRepay is not None:
            data["autoBorrowRepay"] = autoBorrowRepay

        if autoLend is not None:
            data["autoLend"] = autoLend

        if autoLendRedeem is not None:
            data["autoLendRedeem"] = autoLendRedeem

        if stopLossTriggerPrice:
            data["stopLossTriggerPrice"] = stopLossTriggerPrice
        if stopLossTriggerBy:
            data["stopLossTriggerBy"] = stopLossTriggerBy

        if stopLossLimitPrice:
            data["stopLossLimitPrice"] = stopLossLimitPrice

        if takeProfitTriggerPrice:
            data["takeProfitTriggerPrice"] = takeProfitTriggerPrice
        if takeProfitTriggerBy:
            data["takeProfitTriggerBy"] = takeProfitTriggerBy

        if takeProfitLimitPrice:
            data["takeProfitLimitPrice"] = takeProfitLimitPrice

        if triggerQuantity:
            data["triggerQuantity"] = triggerQuantity
        if slippageTolerance is not None:
            data["slippageTolerance"] = slippageTolerance
        if slippageToleranceType is not None:
            data["slippageToleranceType"] = slippageToleranceType

        extra_headers = None
        if brokerId is not None:
            extra_headers = {"X-Broker-Id": str(brokerId)}

        return self._send_request(
            "POST", "api/v1/order", "orderExecute", data, extra_headers=extra_headers
        )

    def cancel_open_order(
        self,
        symbol: str,
        clientId: Optional[int] = None,
        orderId: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Cancels an open order from the order book.

        One of orderId or clientId must be specified.

        Args:
            symbol: Market symbol.
            clientId: Client-provided order ID.
            orderId: Exchange order ID.

        Returns:
            Cancelled order information.
        """
        data = {"symbol": symbol}
        if clientId:
            data["clientId"] = clientId
        if orderId:
            data["orderId"] = orderId
        return self._send_request("DELETE", "api/v1/order", "orderCancel", data)

    def get_open_orders(
        self,
        symbol: Optional[str] = None,
        marketType: Optional[Union[MarketType, str]] = None
    ) -> List[Dict[str, Any]]:
        """
        Retrieves all open orders.

        Args:
            symbol: Optional market symbol filter.
            marketType: Optional market type filter (SPOT, PERP, etc.).

        Returns:
            List of open orders.
        """
        params = {}
        if symbol:
            params["symbol"] = symbol
        if marketType:
            params["marketType"] = (
                marketType.value if isinstance(marketType, MarketType) else marketType
            )
        return self._send_request("GET", "api/v1/orders", "orderQueryAll", params)

    def cancel_open_orders(
        self,
        symbol: str,
        orderType: Optional[Union[CancelOrderType, str]] = None
    ) -> List[Dict[str, Any]]:
        """
        Cancels all open orders on the specified market.

        Args:
            symbol: Market symbol.
            orderType: Type of orders to cancel (RestingLimitOrder or ConditionalOrder).

        Returns:
            List of cancelled orders.
        """
        params = {"symbol": symbol}
        if orderType:
            params["orderType"] = (
                orderType.value if isinstance(orderType, CancelOrderType) else orderType
            )
        return self._send_request("DELETE", "api/v1/orders", "orderCancelAll", params)

    def execute_batch_orders(
        self,
        orders: List[Dict[str, Any]],
        brokerId: Optional[int] = None,
    ) -> List[Dict[str, Any]]:
        """
        Submits a batch of orders for execution.

        Each order in the list should contain the same parameters as execute_order.

        Args:
            orders: List of order dictionaries. Each order should contain:
                - orderType: 'Market' or 'Limit'
                - side: 'Bid' or 'Ask'
                - symbol: Market symbol
                - price: Price for limit orders
                - quantity: Order quantity
                - And other optional parameters
            brokerId: Optional broker ID.

        Returns:
            List of order execution results.

        Example:
            orders = [
                {
                    "symbol": "SOL_USDC_PERP",
                    "side": "Bid",
                    "orderType": "Limit",
                    "price": "141",
                    "quantity": "12"
                },
                {
                    "symbol": "SOL_USDC_PERP",
                    "side": "Bid",
                    "orderType": "Limit",
                    "price": "140",
                    "quantity": "11"
                }
            ]
            results = client.execute_batch_orders(orders)
        """
        extra_headers = None
        if brokerId is not None:
            extra_headers = {"X-Broker-Id": str(brokerId)}
        return self._send_batch_request("api/v1/orders", orders, extra_headers=extra_headers)
