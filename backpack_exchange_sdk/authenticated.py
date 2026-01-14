"""
Authenticated client for Backpack Exchange API.

This module provides the AuthenticationClient class which handles all authenticated
API endpoints including account management, orders, capital operations, and more.
"""

import base64
from typing import Any, Dict, List, Optional, Union

from backpack_exchange_sdk._base.client import AuthenticatedBaseClient
from backpack_exchange_sdk._mixins.account import AccountMixin
from backpack_exchange_sdk._mixins.borrow_lend import BorrowLendMixin
from backpack_exchange_sdk._mixins.capital import CapitalMixin
from backpack_exchange_sdk._mixins.history import HistoryMixin
from backpack_exchange_sdk._mixins.order import OrderMixin
from backpack_exchange_sdk._mixins.rfq import RFQMixin
from backpack_exchange_sdk._mixins.strategy import StrategyMixin


class AuthenticationClient(
    AccountMixin,
    CapitalMixin,
    OrderMixin,
    BorrowLendMixin,
    HistoryMixin,
    RFQMixin,
    StrategyMixin,
    AuthenticatedBaseClient,
):
    """
    Authenticated client for Backpack Exchange API.

    This client provides access to all authenticated endpoints including:
    - Account management
    - Order execution and management
    - Capital operations (deposits, withdrawals)
    - Borrow/Lend operations
    - Historical data queries
    - RFQ (Request For Quote) operations
    - Strategy operations

    Args:
        public_key: Your Backpack Exchange API public key.
        secret_key: Your Backpack Exchange API secret key (base64 encoded).
        window: Request validity window in milliseconds (default: 5000).

    Example:
        >>> client = AuthenticationClient(
        ...     public_key="your_public_key",
        ...     secret_key="your_secret_key"
        ... )
        >>> account = client.get_account()
    """

    # Class attribute for backward compatibility
    base_url = "https://api.backpack.exchange/"

    def __init__(self, public_key: str, secret_key: str, window: int = 5000):
        """
        Initialize the authenticated client.

        Args:
            public_key: Your Backpack Exchange API public key.
            secret_key: Your Backpack Exchange API secret key (base64 encoded).
            window: Request validity window in milliseconds (default: 5000).
        """
        super().__init__(public_key, secret_key, window)

    def _sign_message(self, message: str) -> str:
        """
        Sign a message with the private key.

        Args:
            message: The message to sign.

        Returns:
            Base64 encoded signature.
        """
        return base64.b64encode(self.private_key_obj.sign(message.encode())).decode()
