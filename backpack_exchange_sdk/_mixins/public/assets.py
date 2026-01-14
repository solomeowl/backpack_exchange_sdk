"""
Assets mixin for PublicClient.
"""

from typing import Any, Dict, List


class AssetsMixin:
    """Mixin providing assets and collateral data operations."""

    def get_assets(self) -> List[Dict[str, Any]]:
        """
        Retrieves all the assets that are supported by the exchange.

        Returns:
            List of asset information dictionaries.
        """
        return self._get("api/v1/assets")

    def get_collateral(self) -> List[Dict[str, Any]]:
        """
        Get collateral parameters for assets.

        Returns:
            List of collateral parameter dictionaries.
        """
        return self._get("api/v1/collateral")
