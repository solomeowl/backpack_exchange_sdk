"""
Borrow/Lend markets mixin for PublicClient.
"""

from typing import Any, Dict, List, Optional


class BorrowLendMarketsMixin:
    """Mixin providing public borrow/lend market data operations."""

    def get_borrow_lend_markets(self) -> List[Dict[str, Any]]:
        """
        Get all borrow lend markets information.

        Returns:
            List of dictionaries containing market information including state,
            interest rates, quantities, utilization rates and other parameters
            for each market.
        """
        return self._get("api/v1/borrowLend/markets")

    def get_borrow_lend_market_history(
        self,
        interval: str,
        symbol: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Get borrow lend market history for specified interval and optional symbol.

        Args:
            interval: Time interval - must be one of: "1d", "1w", "1month", "1year".
            symbol: Market symbol to query. If not set, all markets are returned.

        Returns:
            Historical borrow lend market data for the specified interval and symbol.
        """
        params = {"interval": interval}
        if symbol:
            params["symbol"] = symbol
        return self._get("api/v1/borrowLend/markets/history", params=params)
