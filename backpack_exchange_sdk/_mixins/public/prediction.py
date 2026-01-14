"""
Prediction markets mixin for PublicClient.
"""

from typing import Any, Dict, List, Optional


class PredictionMixin:
    """Mixin providing prediction market data operations."""

    def get_prediction_markets(
        self,
        symbol: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Get prediction markets information.

        Args:
            symbol: Market symbol to filter. If not set, all markets are returned.

        Returns:
            List of prediction markets with their information.
        """
        params = {}
        if symbol:
            params["symbol"] = symbol
        return self._get("api/v1/prediction", params=params if params else None)

    def get_prediction_tags(self) -> List[Dict[str, Any]]:
        """
        Get available prediction market tags.

        Returns:
            List of prediction market tags.
        """
        return self._get("api/v1/prediction/tags")
