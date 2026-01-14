"""
Public trades mixin for PublicClient.
"""

from typing import Any, Dict, List


class TradesMixin:
    """Mixin providing public trade data operations."""

    def get_recent_trades(self, symbol: str, limit: int = 100) -> List[Dict[str, Any]]:
        """
        Retrieve the most recent trades for a symbol.

        This is public data and is not specific to any account.
        The maximum available recent trades is 1000. If you need more than
        1000 trades use the historical trades endpoint.

        Args:
            symbol: Market symbol.
            limit: Maximum results (default: 100, max: 1000).

        Returns:
            List of recent trade records.
        """
        params = {"symbol": symbol, "limit": limit}
        return self._get("api/v1/trades", params=params)

    def get_historical_trades(
        self,
        symbol: str,
        limit: int = 100,
        offset: int = 0
    ) -> List[Dict[str, Any]]:
        """
        Retrieves all historical trades for the given symbol.

        This is public trade data and is not specific to any account.

        Args:
            symbol: Market symbol.
            limit: Maximum results (default: 100).
            offset: Pagination offset.

        Returns:
            List of historical trade records.
        """
        params = {"symbol": symbol, "limit": limit, "offset": offset}
        return self._get("api/v1/trades/history", params=params)
