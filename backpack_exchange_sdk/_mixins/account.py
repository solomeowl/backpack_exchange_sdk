"""
Account operations mixin for AuthenticationClient.
"""

from typing import Any, Dict, Optional


class AccountMixin:
    """Mixin providing account-related operations."""

    def get_account(self) -> Dict[str, Any]:
        """
        Retrieves account settings.

        Returns:
            Account settings and information.
        """
        return self._send_request("GET", "api/v1/account", "accountQuery")

    def update_account(
        self,
        autoBorrowSettlements: Optional[bool] = None,
        autoLend: Optional[bool] = None,
        autoRepayBorrows: Optional[bool] = None,
        leverageLimit: Optional[str] = None,
    ) -> None:
        """
        Update account settings.

        Args:
            autoBorrowSettlements: Enable auto borrow for settlements
            autoLend: Enable auto lending
            autoRepayBorrows: Enable auto repay borrows
            leverageLimit: Maximum leverage limit
        """
        data = {}
        if autoBorrowSettlements is not None:
            data["autoBorrowSettlements"] = autoBorrowSettlements
        if autoLend is not None:
            data["autoLend"] = autoLend
        if autoRepayBorrows is not None:
            data["autoRepayBorrows"] = autoRepayBorrows
        if leverageLimit is not None:
            data["leverageLimit"] = leverageLimit

        self._send_request("PATCH", "api/v1/account", "accountUpdate", data)

    def get_max_borrow_quantity(self, symbol: str) -> Dict[str, Any]:
        """
        Retrieves the maximum quantity an account can borrow for a given asset.

        Args:
            symbol: The asset symbol to borrow.

        Returns:
            Maximum borrow quantity information.
        """
        return self._send_request(
            "GET", "api/v1/account/limits/borrow", "maxBorrowQuantity",
            params={"symbol": symbol}
        )

    def get_max_order_quantity(
        self,
        symbol: str,
        side: str,
        price: Optional[str] = None,
        reduceOnly: Optional[bool] = None,
        autoBorrow: Optional[bool] = None,
        autoBorrowRepay: Optional[bool] = None,
        autoLendRedeem: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """
        Retrieves the maximum quantity an account can trade for a given symbol.

        Args:
            symbol: The market symbol to trade.
            side: Order side ('Bid' or 'Ask').
            price: Optional limit price for the order.
            reduceOnly: Whether the order is reduce-only.
            autoBorrow: Whether to use auto borrow.
            autoBorrowRepay: Whether to use auto borrow repay.
            autoLendRedeem: Whether to use auto lend redeem.

        Returns:
            Maximum order quantity information.
        """
        params = {"symbol": symbol, "side": side}

        if price is not None:
            params["price"] = price
        if reduceOnly is not None:
            params["reduceOnly"] = reduceOnly
        if autoBorrow is not None:
            params["autoBorrow"] = autoBorrow
        if autoBorrowRepay is not None:
            params["autoBorrowRepay"] = autoBorrowRepay
        if autoLendRedeem is not None:
            params["autoLendRedeem"] = autoLendRedeem

        return self._send_request(
            "GET", "api/v1/account/limits/order", "maxOrderQuantity", params
        )

    def get_max_withdrawal_quantity(
        self,
        symbol: str,
        autoBorrow: Optional[bool] = None,
        autoLendRedeem: Optional[bool] = None
    ) -> Dict[str, Any]:
        """
        Retrieves the maximum quantity an account can withdraw for a given asset.

        Args:
            symbol: The asset symbol to withdraw.
            autoBorrow: Whether the withdrawal uses auto borrow.
            autoLendRedeem: Whether the withdrawal uses auto lend redeem.

        Returns:
            Maximum withdrawal quantity information.
        """
        params = {"symbol": symbol}

        if autoBorrow is not None:
            params["autoBorrow"] = autoBorrow
        if autoLendRedeem is not None:
            params["autoLendRedeem"] = autoLendRedeem

        return self._send_request(
            "GET", "api/v1/account/limits/withdrawal", "maxWithdrawalQuantity", params
        )
