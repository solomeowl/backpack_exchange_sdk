"""
Borrow/Lend operations mixin for AuthenticationClient.
"""

from typing import Any, Dict, List, Optional


class BorrowLendMixin:
    """Mixin providing borrow/lend related operations."""

    def get_borrow_lend_positions(self) -> List[Dict[str, Any]]:
        """
        Retrieves all open borrow/lending positions for the account.

        Returns:
            List of borrow/lend positions.
        """
        return self._send_request(
            "GET", "api/v1/borrowLend/positions", "borrowLendPositionQuery"
        )

    def execute_borrow_lend(
        self,
        quantity: str,
        side: str,
        symbol: str
    ) -> None:
        """
        Execute a borrow or lend operation.

        Args:
            quantity: Amount to borrow or lend.
            side: 'Borrow' or 'Lend'.
            symbol: Asset symbol.
        """
        data = {"quantity": quantity, "side": side, "symbol": symbol}
        self._send_request("POST", "api/v1/borrowLend", "borrowLendExecute", data)

    def get_estimated_liquidation_price(
        self,
        borrow: str,
        subaccountId: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Retrieves the estimated liquidation price for a potential borrow/lend position.

        Args:
            borrow: Base64 encoded JSON of BorrowLendExecutePayload.
            subaccountId: Optional subaccount ID.

        Returns:
            Estimated liquidation price information.
        """
        params = {"borrow": borrow}
        if subaccountId is not None:
            params["subaccountId"] = subaccountId
        return self._send_request(
            "GET", "api/v1/borrowLend/position/liquidationPrice",
            "borrowLendPositionLiquidationPrice", params
        )

    def get_open_positions(
        self,
        symbol: Optional[str] = None,
        marketType: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Retrieves account position summary.

        Args:
            symbol: Optional market symbol filter.
            marketType: Optional market type filter.

        Returns:
            List of open positions.
        """
        params = {}
        if symbol:
            params["symbol"] = symbol
        if marketType:
            params["marketType"] = marketType
        return self._send_request("GET", "api/v1/position", "positionQuery", params)
