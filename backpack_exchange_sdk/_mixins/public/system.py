"""
System status mixin for PublicClient.
"""

from typing import Any, Dict, List


class SystemMixin:
    """Mixin providing system status operations."""

    def get_status(self) -> Dict[str, Any]:
        """
        Get the system status, and the status message, if any.

        Returns:
            System status information.
        """
        return self._get("api/v1/status")

    def send_ping(self) -> str:
        """
        Responds with pong.

        Returns:
            'pong' string.
        """
        return self._get("api/v1/ping")

    def get_system_time(self) -> str:
        """
        Retrieves the current system time.

        Returns:
            Current server timestamp.
        """
        return self._get("api/v1/time")

    def get_wallets(self) -> List[Dict[str, Any]]:
        """
        Get supported wallets for deposits/withdrawals.

        Returns:
            List of wallet configurations with blockchain addresses.
        """
        return self._get("api/v1/wallets")
