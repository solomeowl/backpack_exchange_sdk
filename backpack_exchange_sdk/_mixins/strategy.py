"""
Strategy operations mixin for AuthenticationClient.
"""

from typing import Any, Dict, List, Optional, Union

from backpack_exchange_sdk.enums import MarketType


class StrategyMixin:
    """Mixin providing strategy-related operations."""

    def create_strategy(
        self,
        symbol: str,
        side: str,
        strategyType: str,
        quantity: str,
        intervalMs: int,
        subOrders: int,
        clientStrategyId: Optional[int] = None,
        slippageTolerance: Optional[str] = None,
        slippageToleranceType: Optional[str] = None,
        reduceOnly: Optional[bool] = None,
        autoBorrow: Optional[bool] = None,
        autoBorrowRepay: Optional[bool] = None,
        autoLend: Optional[bool] = None,
        autoLendRedeem: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """
        Create a new strategy.

        Args:
            symbol: Market symbol.
            side: Order side ('Bid' or 'Ask').
            strategyType: Strategy type (e.g., 'Scheduled').
            quantity: Total quantity to execute.
            intervalMs: Interval between sub-orders in milliseconds.
            subOrders: Number of sub-orders to split the quantity into.
            clientStrategyId: Optional client-provided strategy ID.
            slippageTolerance: Maximum slippage tolerance.
            slippageToleranceType: Slippage tolerance type ('TickSize' or 'Percent').
            reduceOnly: Whether orders are reduce-only.
            autoBorrow: Enable auto borrow.
            autoBorrowRepay: Enable auto borrow repay.
            autoLend: Enable auto lend.
            autoLendRedeem: Enable auto lend redeem.

        Returns:
            Strategy details including strategyId, status, etc.
        """
        data = {
            "symbol": symbol,
            "side": side,
            "strategyType": strategyType,
            "quantity": quantity,
            "intervalMs": intervalMs,
            "subOrders": subOrders,
        }
        if clientStrategyId is not None:
            data["clientStrategyId"] = clientStrategyId
        if slippageTolerance is not None:
            data["slippageTolerance"] = slippageTolerance
        if slippageToleranceType is not None:
            data["slippageToleranceType"] = slippageToleranceType
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

        return self._send_request("POST", "api/v1/strategy", "strategyCreate", data)

    def get_strategy(
        self,
        symbol: str,
        strategyId: Optional[str] = None,
        clientStrategyId: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Get an open strategy.

        One of strategyId or clientStrategyId must be specified.

        Args:
            symbol: Market symbol.
            strategyId: Exchange strategy ID.
            clientStrategyId: Client-provided strategy ID.

        Returns:
            Strategy information.
        """
        params = {"symbol": symbol}
        if strategyId:
            params["strategyId"] = strategyId
        if clientStrategyId is not None:
            params["clientStrategyId"] = clientStrategyId
        return self._send_request("GET", "api/v1/strategy", "strategyQuery", params)

    def cancel_strategy(
        self,
        symbol: str,
        strategyId: Optional[str] = None,
        clientStrategyId: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Cancel an open strategy.

        One of strategyId or clientStrategyId must be specified.

        Args:
            symbol: Market symbol.
            strategyId: Exchange strategy ID.
            clientStrategyId: Client-provided strategy ID.

        Returns:
            Cancelled strategy information.
        """
        data = {"symbol": symbol}
        if strategyId:
            data["strategyId"] = strategyId
        if clientStrategyId is not None:
            data["clientStrategyId"] = clientStrategyId
        return self._send_request("DELETE", "api/v1/strategy", "strategyCancel", data)

    def get_open_strategies(
        self,
        symbol: Optional[str] = None,
        marketType: Optional[Union[MarketType, str]] = None,
    ) -> List[Dict[str, Any]]:
        """
        Get all open strategies.

        Args:
            symbol: Optional market symbol filter.
            marketType: Optional market type filter.

        Returns:
            List of open strategies.
        """
        params = {}
        if symbol:
            params["symbol"] = symbol
        if marketType:
            params["marketType"] = (
                marketType.value if isinstance(marketType, MarketType) else marketType
            )
        return self._send_request("GET", "api/v1/strategies", "strategyQueryAll", params)

    def cancel_all_strategies(self, symbol: str) -> List[Dict[str, Any]]:
        """
        Cancel all open strategies for a market.

        Args:
            symbol: Market symbol.

        Returns:
            List of cancelled strategies.
        """
        data = {"symbol": symbol}
        return self._send_request("DELETE", "api/v1/strategies", "strategyCancelAll", data)
