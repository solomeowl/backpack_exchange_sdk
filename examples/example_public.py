from backpack_exchange_sdk.public import PublicClient
public_client = PublicClient()

# get assets
print(public_client.get_assets())

# get markets
print(public_client.get_markets())

# get ticker
print(public_client.get_ticker('SOL_USDC'))

# get tickers
print(public_client.get_tickers())

# get order book depth
print(public_client.get_order_book_depth('SOL_USDC'))

# get klines
print(public_client.get_klines('SOL_USDC', '1m'))

# get status
print(public_client.get_status())

# send ping
print(public_client.send_ping())

# get system time
print(public_client.get_system_time())

# get recent trades
print(public_client.get_recent_trades('SOL_USDC'))

# get historical trades
print(public_client.get_historical_trades('SOL_USDC',10,0))
