"""
Market data mixin for PublicClient.
"""

from typing import Any, Dict, List, Optional, Union

from backpack_exchange_sdk.enums import TickerInterval


class MarketMixin:
    """Mixin providing public market data operations."""

    def get_markets(self) -> List[Dict[str, Any]]:
        """
        Retrieves all the markets that are supported by the exchange.

        Returns:
            List of market information dictionaries.
        """
        return self._get("api/v1/markets")

    def get_market(self, symbol: str) -> Dict[str, Any]:
        """
        Retrieves a market supported by the exchange.

        Args:
            symbol: Market symbol (e.g., 'SOL_USDC').

        Returns:
            Market information dictionary.
        """
        return self._get("api/v1/market", params={"symbol": symbol})

    def get_ticker(
        self,
        symbol: str,
        interval: Union[TickerInterval, str] = TickerInterval.D1
    ) -> Dict[str, Any]:
        """
        Retrieves summarised statistics for the last 24 hours for the given market symbol.

        Args:
            symbol: Market symbol.
            interval: Ticker interval (default: 1 day).

        Returns:
            Ticker statistics dictionary.
        """
        interval_value = interval.value if isinstance(interval, TickerInterval) else interval
        params = {"symbol": symbol, "interval": interval_value}
        return self._get("api/v1/ticker", params=params)

    def get_tickers(
        self,
        interval: Union[TickerInterval, str] = TickerInterval.D1
    ) -> List[Dict[str, Any]]:
        """
        Retrieves summarised statistics for the last 24 hours for all market symbols.

        Args:
            interval: Ticker interval (default: 1 day).

        Returns:
            List of ticker statistics dictionaries.
        """
        interval_value = interval.value if isinstance(interval, TickerInterval) else interval
        params = {"interval": interval_value}
        return self._get("api/v1/tickers", params=params)

    def get_depth(self, symbol: str) -> Dict[str, Any]:
        """
        Retrieves the order book depth for a given market symbol.

        Args:
            symbol: Market symbol.

        Returns:
            Order book depth with bids and asks.
        """
        return self._get("api/v1/depth", params={"symbol": symbol})

    def get_klines(
        self,
        symbol: str,
        interval: str,
        start_time: int,
        end_time: Optional[int] = None
    ) -> List[List[Any]]:
        """
        Get K-Lines (candlestick data) for the given market symbol.

        Args:
            symbol: Market symbol.
            interval: Kline interval (e.g., '1m', '1h', '1d').
            start_time: Start timestamp in milliseconds.
            end_time: End timestamp in milliseconds (default: current time).

        Returns:
            List of kline data arrays.
        """
        params = {"symbol": symbol, "interval": interval, "startTime": start_time}
        if end_time is not None:
            params["endTime"] = end_time
        return self._get("api/v1/klines", params=params)

    def get_mark_price(self, symbol: str) -> Dict[str, Any]:
        """
        Retrieves mark price, index price and funding rate for the given market symbol.

        Args:
            symbol: Market symbol (futures).

        Returns:
            Mark price information dictionary.
        """
        return self._get("api/v1/markPrices", params={"symbol": symbol})

    def get_open_interest(self, symbol: str) -> Dict[str, Any]:
        """
        Retrieves the current open interest for the given market.

        Args:
            symbol: Market symbol (futures).

        Returns:
            Open interest information.
        """
        return self._get("api/v1/openInterest", params={"symbol": symbol})

    def get_funding_interval_rates(
        self,
        symbol: str,
        limit: int = 100,
        offset: int = 0
    ) -> List[Dict[str, Any]]:
        """
        Funding interval rate history for futures.

        Args:
            symbol: Market symbol (futures).
            limit: Maximum results (default: 100).
            offset: Pagination offset.

        Returns:
            List of funding rate records.
        """
        params = {"symbol": symbol, "limit": limit, "offset": offset}
        return self._get("api/v1/fundingRates", params=params)
