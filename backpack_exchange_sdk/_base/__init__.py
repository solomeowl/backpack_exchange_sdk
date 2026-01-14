"""
Internal base classes for Backpack Exchange SDK.
"""

from backpack_exchange_sdk._base.errors import BackpackAPIError, BackpackRequestError
from backpack_exchange_sdk._base.client import BaseClient, AuthenticatedBaseClient

__all__ = [
    "BackpackAPIError",
    "BackpackRequestError",
    "BaseClient",
    "AuthenticatedBaseClient",
]
