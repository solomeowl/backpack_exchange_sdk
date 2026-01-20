"""
Public client for Backpack Exchange API.

This module provides the PublicClient class which handles all public
API endpoints that don't require authentication.
"""

from typing import Optional, List

from backpack_exchange_sdk._base.client import BaseClient
from backpack_exchange_sdk._mixins.public.assets import AssetsMixin
from backpack_exchange_sdk._mixins.public.borrow_lend_markets import BorrowLendMarketsMixin
from backpack_exchange_sdk._mixins.public.market import MarketMixin
from backpack_exchange_sdk._mixins.public.prediction import PredictionMixin
from backpack_exchange_sdk._mixins.public.system import SystemMixin
from backpack_exchange_sdk._mixins.public.trades import TradesMixin


class PublicClient(
    AssetsMixin,
    MarketMixin,
    SystemMixin,
    TradesMixin,
    BorrowLendMarketsMixin,
    PredictionMixin,
    BaseClient,
):
    """
    Public client for Backpack Exchange API.

    This client provides access to all public endpoints including:
    - Asset information
    - Market data (tickers, depth, klines)
    - System status
    - Public trade data
    - Borrow/Lend market data
    - Prediction market data

    No authentication is required for these endpoints.

    Example:
        >>> client = PublicClient()
        >>> markets = client.get_markets()
        >>> ticker = client.get_ticker("SOL_USDC")
    """

    def __init__(
        self,
        base_url: str = None,
        timeout: float = None,
        max_retries: int = 0,
        backoff_factor: float = 0.1,
        status_forcelist: Optional[List[int]] = None,
    ):
        """Initialize the public client."""
        super().__init__(
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
            backoff_factor=backoff_factor,
            status_forcelist=status_forcelist,
        )
