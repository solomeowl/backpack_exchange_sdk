"""
Backpack Exchange SDK

A Python SDK for interacting with the Backpack Exchange API.

Example usage:
    >>> from backpack_exchange_sdk import AuthenticationClient, PublicClient
    >>>
    >>> # Public endpoints (no authentication required)
    >>> public = PublicClient()
    >>> markets = public.get_markets()
    >>>
    >>> # Authenticated endpoints
    >>> client = AuthenticationClient(
    ...     public_key="your_public_key",
    ...     secret_key="your_secret_key"
    ... )
    >>> account = client.get_account()
"""

from backpack_exchange_sdk.authenticated import AuthenticationClient
from backpack_exchange_sdk.public import PublicClient

# WebSocket client for real-time data
try:
    from backpack_exchange_sdk.websocket import WebSocketClient
except ImportError:
    WebSocketClient = None  # websocket-client may not be installed

__version__ = "1.1.3"
__all__ = [
    "AuthenticationClient",
    "PublicClient",
    "WebSocketClient",
    "__version__",
]
