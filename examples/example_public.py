from backpack_exchange_sdk.public import PublicClient
public_client = PublicClient()

# Get assets
print(public_client.get_assets())

# Get collateral parameters for assets
print(public_client.get_collateral())

# ================================================================
# Market - Public market data.
# ================================================================
# Get all markets
print(public_client.get_markets())

# Get specific market
print(public_client.get_market('SOL_USDC'))

# Get ticker for a specific market
print(public_client.get_ticker('SOL_USDC'))

# Get tickers for all markets
print(public_client.get_tickers())

# Get order book depth for a specific market
print(public_client.get_depth('SOL_USDC'))

# Get K-Lines for a specific market
print(public_client.get_klines('SOL_USDC', '1m'))

# Get mark price for a specific market
print(public_client.get_mark_price('SOL_USDC'))

# Get open interest for a specific market
print(public_client.get_open_interest('SOL_USDC'))

# Get funding interval rates for a specific market
print(public_client.get_funding_interval_rates('SOL_USDC'))

# ================================================================
# System - Exchange system status.
# ================================================================
# Get system status
print(public_client.get_status())

# Send ping
print(public_client.send_ping())

# Get system time
print(public_client.get_system_time())

# ================================================================
# Trades - Public trade data.
# ================================================================
# Get recent trades for a specific market
print(public_client.get_recent_trades('SOL_USDC'))

# Get historical trades for a specific market
print(public_client.get_historical_trades('SOL_USDC', 10, 0))
