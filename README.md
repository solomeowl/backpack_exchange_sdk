# Backpack Exchange SDK
![PyPI - Version](https://img.shields.io/pypi/v/backpack-exchange-sdk?)

The Backpack Exchange SDK provides a convenient interface for interacting with the Backpack Exchange API. It includes three main clients: `AuthenticationClient` for authenticated endpoints, `PublicClient` for public endpoints, and `WebSocketClient` for real-time data streaming.

## Features

- **Authentication Client**: Interact with authenticated endpoints for managing capital, historical data, and orders.
- **Public Client**: Access public market data, system status, and public trade data.
- **WebSocket Client**: Stream real-time market data and account updates.

## Installation

The SDK can be installed directly using pip:

```bash
pip3 install backpack_exchange_sdk
```

Alternatively, you can clone the repository and install the SDK manually:

```bash
git clone https://github.com/solomeowl/backpack_exchange_sdk.git
cd backpack_exchange_sdk
pip3 install .
```

## Usage
### Authentication Client
```python
from backpack_exchange_sdk.authenticated import AuthenticationClient

client = AuthenticationClient('<YOUR_API_KEY>', '<YOUR_SECRET>')

# Get account balances
balances = client.get_balances()
print(balances)

# Request a withdrawal
response = client.request_withdrawal('xxxxaddress', 'Solana', '0,1', 'Sol')
print(response)
```

### Public Client
```python
from backpack_exchange_sdk.public import PublicClient

public_client = PublicClient()

# Get all supported assets
assets = public_client.get_assets()
print(assets)

# Get ticker information for a specific symbol
ticker = public_client.get_ticker('SOL_USDC')
print(ticker)
```

### WebSocket Client
```python
from backpack_exchange_sdk.websocket import WebSocketClient
from datetime import datetime

# Initialize WebSocket client
ws_client = WebSocketClient()  # For public streams only
# ws_client = WebSocketClient(api_key='<YOUR_API_KEY>', secret_key='<YOUR_SECRET>')  # For private streams

# Define callback functions
def handle_book_ticker(data):
    """Handle book ticker updates"""
    print("\n=== Book Ticker Update ===")
    print(f"Symbol: {data['s']}")
    print(f"Best Ask: {data['a']} (Quantity: {data['A']})")
    print(f"Best Bid: {data['b']} (Quantity: {data['B']})")
    print(f"Time: {datetime.fromtimestamp(data['E']/1000000).strftime('%Y-%m-%d %H:%M:%S.%f')}")

def handle_trades(data):
    """Handle trade updates"""
    print("\n=== Trade Update ===")
    print(f"Symbol: {data['s']}")
    print(f"Price: {data['p']}")
    print(f"Quantity: {data['q']}")
    print(f"Trade Type: {'Maker' if data['m'] else 'Taker'}")
    print(f"Trade ID: {data['t']}")

def handle_kline(data):
    """Handle kline/candlestick updates"""
    print("\n=== Kline Update ===")
    print(f"Symbol: {data['s']}")
    print(f"Open: {data['o']}")
    print(f"High: {data['h']}")
    print(f"Low: {data['l']}")
    print(f"Close: {data['c']}")
    print(f"Volume: {data['v']}")
    print(f"Closed: {data['X']}")

# Subscribe to public streams
ws_client.subscribe(
    streams=["bookTicker.SOL_USDC"],  # Book ticker stream
    callback=handle_book_ticker
)

# Subscribe to private streams (requires authentication)
ws_client.subscribe(
    streams=["account.orderUpdate.SOL_USDC"],  # Order updates stream
    callback=handle_trades,
    is_private=True
)

# Keep the connection alive
import time
while True:
    time.sleep(1)
```

## Documentation
For more detailed information about the API endpoints and their usage, refer to the [Backpack Exchange API documentation](https://docs.backpack.exchange/).

## Support 

If this SDK has been helpful to you 🌟 and you haven't signed up for Backpack Exchange yet, please consider using the following referral link to register: [Register on Backpack Exchange](https://backpack.exchange/refer/solomeowl) 🚀.

Using this referral link is a great way to support this project ❤️, as it helps to grow the community and ensures the continued development of the SDK. 🛠️
