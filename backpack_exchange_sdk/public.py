import requests


class PublicClient:
    def __init__(self):
        self.base_url = 'https://api.backpack.exchange/'

    # ================================================================
    # Assets - Assets and collateral data.
    # ================================================================
    def get_assets(self):
        """
        Retrieves all the assets that are supported by the exchange.
        """
        return requests.get(url=f'{self.base_url}api/v1/assets').json()

    def get_collateral(self):
        """
        Get collateral parameters for assets.
        """
        return requests.get(url=f'{self.base_url}api/v1/collateral').json()

    # ================================================================
    # Market - Public market data.
    # ================================================================
    def get_markets(self):
        """
        Retrieves all the markets that are supported by the exchange.
        """
        return requests.get(url=f'{self.base_url}api/v1/markets').json()

    def get_market(self, symbol: str):
        """
        Retrieves a market supported by the exchange.
        """
        return requests.get(url=f'{self.base_url}api/v1/market', params={'symbol': symbol}).json()

    def get_ticker(self, symbol: str):
        """
        Retrieves summarised statistics for the last 24 hours for the given market symbol.
        """
        return requests.get(url=f'{self.base_url}api/v1/ticker', params={'symbol': symbol}).json()

    def get_tickers(self):
        """
        Retrieves summarised statistics for the last 24 hours for all market symbols.
        """
        return requests.get(url=f'{self.base_url}api/v1/tickers').json()

    def get_depth(self, symbol: str):
        """
        Retrieves the order book depth for a given market symbol.
        """
        return requests.get(url=f'{self.base_url}api/v1/depth', params={'symbol': symbol}).json()

    def get_klines(self, symbol: str, interval: str, start_time: int = 0, end_time: int = 0):
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
        return requests.get(url=f'{self.base_url}api/v1/klines', params=params).json()

    def get_mark_price(self, symbol: str):
        """
        Retrieves mark price, index price and funding rate for the given market symbol.
        """
        return requests.get(url=f'{self.base_url}api/v1/markPrice', params={'symbol': symbol}).json()

    def get_open_interest(self, symbol: str):
        """
        Retrieves the current open interest for the given market.
        """
        return requests.get(url=f'{self.base_url}api/v1/openInterest', params={'symbol': symbol}).json()

    def get_funding_interval_rates(self, symbol: str, limit: int = 100, offset: int = 0):
        """
        Funding interval rate history for futures.
        """
        params = {'symbol': symbol, 'limit': limit, 'offset': offset}
        return requests.get(url=f'{self.base_url}api/v1/fundingRates', params=params).json()


    # ================================================================
    # System - Exchange system status.
    # ================================================================
    def get_status(self):
        """
        Get the system status, and the status message, if any.
        """
        return requests.get(url=f'{self.base_url}api/v1/status').json()

    def send_ping(self):
        """
        Responds with pong.
        """
        return requests.get(url=f'{self.base_url}api/v1/ping').text

    def get_system_time(self):
        """
        Retrieves the current system time.
        """
        return requests.get(url=f'{self.base_url}api/v1/time').text

    # ================================================================
    # Trades - Public trade data.
    # ================================================================
    def get_recent_trades(self, symbol: str, limit: int = 100):
        """
        Retrieve the most recent trades for a symbol. This is public data and is not specific to any account.
        The maximum available recent trades is 1000. If you need more than 1000 trades use the historical trades
        endpoint.
        """
        params = {'symbol': symbol, 'limit': limit}
        return requests.get(url=f'{self.base_url}api/v1/trades', params=params).json()

    def get_historical_trades(self, symbol: str, limit: int = 100, offset: int = 0):
        """
        Retrieves all historical trades for the given symbol. This is public trade data and is not specific to any
        account.
        """
        params = {'symbol': symbol, 'limit': limit, 'offset': offset}
        return requests.get(url=f'{self.base_url}api/v1/trades/history', params=params).json()
