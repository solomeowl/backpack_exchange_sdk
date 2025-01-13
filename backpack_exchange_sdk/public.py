import requests
from typing import List
from .models import Asset, ApiError, CollateralInfo, Market, Ticker, Depth, Kline, MarkPrice, OpenInterest, FundingRate, SystemStatus, Trade  # 匯入模型
from pydantic import ValidationError


class PublicClient:
    def __init__(self):
        self.base_url = 'https://api.backpack.exchange/'

    def _get(self, endpoint, params=None):
        response = requests.get(url=f'{self.base_url}{endpoint}', params=params)
        if 200 <= response.status_code < 300:  
            if response.status_code == 204: 
                return None
            try:
                return response.json()
            except ValueError:
                return response.text
        else:
            try:
                error = ApiError(**response.json())
                raise Exception(f"API Error: {error.code} - {error.message}")
            except (ValueError, ValidationError):
                raise Exception(f"HTTP Error {response.status_code}: {response.text}")

    def get_assets(self) -> List[Asset]:
        """
        Retrieves all the assets that are supported by the exchange.
        """
        response_data = self._get('api/v1/assets')
        return [Asset(**item) for item in response_data]

    def get_collateral(self) -> List[CollateralInfo]:
        """
        Get collateral parameters for assets.
        """
        response_data = self._get('api/v1/collateral')
        return [CollateralInfo(**item) for item in response_data]

    # ================================================================
    # Market - Public market data.
    # ================================================================
    def get_markets(self) -> List[Market]:
        """
        Retrieves all the markets that are supported by the exchange.
        """
        response_data = self._get('api/v1/markets')
        return [Market(**item) for item in response_data]

    def get_market(self, symbol: str) -> Market:
        """
        Retrieves a market supported by the exchange.
        """
        response_data = self._get('api/v1/market', params={'symbol': symbol})
        return Market(**response_data)

    def get_ticker(self, symbol: str) -> Ticker:
        """
        Retrieves summarised statistics for the last 24 hours for the given market symbol.
        """
        response_data = self._get('api/v1/ticker', params={'symbol': symbol})
        return Ticker(**response_data)

    def get_tickers(self) -> List[Ticker]:
        """
        Retrieves summarised statistics for the last 24 hours for all market symbols.
        """
        response_data = self._get('api/v1/tickers')
        return [Ticker(**item) for item in response_data]

    def get_depth(self, symbol: str) -> Depth:
        """
        Retrieves the order book depth for a given market symbol.
        """
        response_data = self._get('api/v1/depth', params={'symbol': symbol})
        return Depth(**response_data)

    def get_klines(self, symbol: str, interval: str, start_time: int = 0, end_time: int = 0) -> List[Kline]:
        """
        Get K-Lines for the given market symbol, optionally providing a startTime and endTime.
        If no startTime is provided, the interval duration will be used. If no endTime is provided,
        the current time will be used.
        """
        params = {'symbol': symbol, 'interval': interval}
        if start_time > 0:
            params['startTime'] = start_time
        if end_time > 0:
            params['endTime'] = end_time
        response_data = self._get('api/v1/klines', params=params)
        return [Kline(**item) for item in response_data]

    def get_mark_price(self, symbol: str) -> MarkPrice:
        """
        Retrieves mark price, index price and funding rate for the given market symbol.
        """
        response_data = self._get(
            'api/v1/markPrice', params={'symbol': symbol})
        return MarkPrice(**response_data)

    def get_open_interest(self, symbol: str) -> OpenInterest:
        """
        Retrieves the current open interest for the given market.
        """
        response_data = self._get(
            'api/v1/openInterest', params={'symbol': symbol})
        return OpenInterest(**response_data)

    def get_funding_interval_rates(self, symbol: str, limit: int = 100, offset: int = 0) -> List[FundingRate]:
        """
        Funding interval rate history for futures.
        """
        params = {'symbol': symbol, 'limit': limit, 'offset': offset}
        response_data = self._get('api/v1/fundingRates', params=params)
        return [FundingRate(**item) for item in response_data]


    # ================================================================
    # System - Exchange system status.
    # ================================================================

    def get_status(self) -> SystemStatus:
        """
        Get the system status, and the status message, if any.
        """
        response_data = self._get('api/v1/status')
        return SystemStatus(**response_data)

    def send_ping(self) -> str:
        """
        Responds with pong.
        """
        return self._get('api/v1/ping')

    def get_system_time(self) -> str:
        """
        Retrieves the current system time.
        """
        return self._get('api/v1/time')

    # ================================================================
    # Trades - Public trade data.
    # ================================================================
    def get_recent_trades(self, symbol: str, limit: int = 100) -> List[Trade]:
        """
        Retrieve the most recent trades for a symbol. This is public data and is not specific to any account.
        The maximum available recent trades is 1000. If you need more than 1000 trades use the historical trades
        endpoint.
        """
        params = {'symbol': symbol, 'limit': limit}
        response_data = self._get('api/v1/trades', params=params)
        return [Trade(**item) for item in response_data]

    def get_historical_trades(self, symbol: str, limit: int = 100, offset: int = 0) -> List[Trade]:
        """
        Retrieves all historical trades for the given symbol. This is public trade data and is not specific to any
        account.
        """
        params = {'symbol': symbol, 'limit': limit, 'offset': offset}
        response_data = self._get('api/v1/trades/history', params=params)
        return [Trade(**item) for item in response_data]
