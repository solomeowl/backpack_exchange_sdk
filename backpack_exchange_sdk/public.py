"""
Public client for Backpack Exchange API.

This module provides the PublicClient class which handles all public
API endpoints that don't require authentication.
"""

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

    def __init__(self):
        """Initialize the public client."""
        super().__init__()
