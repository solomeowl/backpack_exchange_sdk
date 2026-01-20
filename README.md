# Backpack Exchange SDK

![PyPI - Version](https://img.shields.io/pypi/v/backpack-exchange-sdk?cacheSeconds=300)
![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/pypi/l/backpack-exchange-sdk?cacheSeconds=300)
![CI](https://github.com/solomeowl/backpack_exchange_sdk/actions/workflows/ci.yml/badge.svg)

**English** | [简体中文](./README_zh-Hans.md) | [繁體中文](./README_zh-Hant.md) | [日本語](./README_ja.md) | [한국어](./README_ko.md) | [Español](./README_es.md) | [Português](./README_pt.md)

A complete Python SDK for the [Backpack Exchange](https://backpack.exchange/) API. Supports all 70 API endpoints including REST and WebSocket.

## Project Docs

- [Changelog](./CHANGELOG.md)
- [Security Policy](./SECURITY.md)
- [Contributing](./CONTRIBUTING.md)

## Features

- **Authentication Client**: Full access to authenticated endpoints (orders, capital, history, RFQ, strategies)
- **Public Client**: Access public market data, system status, and trade data
- **WebSocket Client**: Real-time streaming for market data and account updates
- **Complete Coverage**: All 70 API endpoints implemented
- **Type Hints**: Full type annotations for better IDE support
- **Enums**: Comprehensive enums for type-safe API calls

## Installation

```bash
pip install backpack-exchange-sdk
```

Or install from source:

```bash
git clone https://github.com/solomeowl/backpack_exchange_sdk.git
cd backpack_exchange_sdk
pip install .
```

## Quick Start

### Public Client

```python
from backpack_exchange_sdk import PublicClient

client = PublicClient()

# Get all markets
markets = client.get_markets()

# Get ticker
ticker = client.get_ticker("SOL_USDC")

# Get order book depth
depth = client.get_depth("SOL_USDC")
```

### Authentication Client

```python
from backpack_exchange_sdk import AuthenticationClient

client = AuthenticationClient("<API_KEY>", "<SECRET_KEY>")

# Get account balances
balances = client.get_balances()

# Place an order
order = client.execute_order(
    orderType="Limit",
    side="Bid",
    symbol="SOL_USDC",
    price="100",
    quantity="1"
)

# Get order history
history = client.get_order_history(symbol="SOL_USDC")
```

### Using Enums

```python
from backpack_exchange_sdk import AuthenticationClient
from backpack_exchange_sdk.enums import OrderType, Side, TimeInForce

client = AuthenticationClient("<API_KEY>", "<SECRET_KEY>")

order = client.execute_order(
    orderType=OrderType.LIMIT.value,
    side=Side.BID.value,
    symbol="SOL_USDC",
    price="100",
    quantity="1",
    timeInForce=TimeInForce.GTC.value
)
```

## API Reference

### Public Client Methods

| Category | Method | Description |
|----------|--------|-------------|
| **System** | `get_status()` | Get system status |
| | `send_ping()` | Ping the server |
| | `get_system_time()` | Get server time |
| | `get_wallets()` | Get supported wallets |
| **Assets** | `get_assets()` | Get all assets |
| | `get_collateral()` | Get collateral info |
| **Markets** | `get_markets()` | Get all markets |
| | `get_market(symbol)` | Get specific market |
| | `get_ticker(symbol)` | Get ticker |
| | `get_tickers()` | Get all tickers |
| | `get_depth(symbol)` | Get order book |
| | `get_klines(symbol, interval, startTime)` | Get candlesticks |
| | `get_mark_price(symbol)` | Get mark price |
| | `get_open_interest(symbol)` | Get open interest |
| | `get_funding_interval_rates(symbol)` | Get funding rates |
| **Trades** | `get_recent_trades(symbol)` | Get recent trades |
| | `get_historical_trades(symbol, limit, offset)` | Get trade history |
| **Borrow/Lend** | `get_borrow_lend_markets()` | Get lending markets |
| | `get_borrow_lend_market_history(interval)` | Get lending history |
| **Prediction** | `get_prediction_markets()` | Get prediction markets |
| | `get_prediction_tags()` | Get prediction tags |

### Authentication Client Methods

| Category | Method | Description |
|----------|--------|-------------|
| **Account** | `get_account()` | Get account settings |
| | `update_account(...)` | Update account settings |
| | `get_max_borrow_quantity(symbol)` | Get max borrow amount |
| | `get_max_order_quantity(symbol, side)` | Get max order size |
| | `get_max_withdrawal_quantity(symbol)` | Get max withdrawal |
| **Capital** | `get_balances()` | Get balances |
| | `get_collateral()` | Get collateral |
| | `get_deposits()` | Get deposit history |
| | `get_deposit_address(blockchain)` | Get deposit address |
| | `get_withdrawals()` | Get withdrawal history |
| | `request_withdrawal(...)` | Request withdrawal |
| | `convert_dust(symbol)` | Convert dust to USDC |
| | `get_withdrawal_delay()` | Get withdrawal delay |
| | `create_withdrawal_delay(hours, token)` | Create withdrawal delay |
| | `update_withdrawal_delay(hours, token)` | Update withdrawal delay |
| **Orders** | `execute_order(...)` | Place single order |
| | `execute_batch_orders(orders)` | Place batch orders |
| | `get_users_open_orders(symbol)` | Get user's open orders |
| | `get_open_orders(symbol)` | Get open orders |
| | `cancel_open_order(symbol, orderId)` | Cancel single order |
| | `cancel_open_orders(symbol)` | Cancel all orders |
| **History** | `get_order_history(symbol)` | Get order history |
| | `get_fill_history(symbol)` | Get fill history |
| | `get_borrow_history()` | Get borrow history |
| | `get_interest_history()` | Get interest history |
| | `get_borrow_position_history()` | Get borrow positions |
| | `get_funding_payments()` | Get funding payments |
| | `get_settlement_history()` | Get settlements |
| | `get_dust_history()` | Get dust conversions |
| | `get_position_history()` | Get position history |
| | `get_strategy_history()` | Get strategy history |
| | `get_rfq_history()` | Get RFQ history |
| | `get_quote_history()` | Get quote history |
| | `get_rfq_fill_history()` | Get RFQ fills |
| | `get_quote_fill_history()` | Get quote fills |
| **Borrow/Lend** | `get_borrow_lend_positions()` | Get positions |
| | `execute_borrow_lend(quantity, side, symbol)` | Borrow or lend |
| | `get_estimated_liquidation_price(borrow)` | Get liquidation price |
| **Positions** | `get_open_positions()` | Get open positions |
| **RFQ** | `submit_rfq(symbol, side, quantity)` | Submit RFQ |
| | `submit_quote(rfqId, price)` | Submit quote |
| | `accept_quote(rfqId, quoteId)` | Accept quote |
| | `refresh_rfq(rfqId)` | Refresh RFQ |
| | `cancel_rfq(rfqId)` | Cancel RFQ |
| **Strategy** | `create_strategy(...)` | Create strategy |
| | `get_strategy(symbol, strategyId)` | Get strategy |
| | `get_open_strategies()` | Get open strategies |
| | `cancel_strategy(symbol, strategyId)` | Cancel strategy |
| | `cancel_all_strategies(symbol)` | Cancel all strategies |

### WebSocket Client

```python
from backpack_exchange_sdk import WebSocketClient

# Public streams (no auth required)
ws = WebSocketClient()

# Private streams (auth required)
ws = WebSocketClient(api_key="<API_KEY>", secret_key="<SECRET_KEY>")

# Subscribe to streams
def on_message(data):
    print(data)

ws.subscribe(
    streams=["bookTicker.SOL_USDC"],
    callback=on_message
)

# Private stream example
ws.subscribe(
    streams=["account.orderUpdate"],
    callback=on_message,
    is_private=True
)
```

## Available Enums

```python
from backpack_exchange_sdk.enums import (
    # Order related
    OrderType,          # Limit, Market
    Side,               # Bid, Ask
    TimeInForce,        # GTC, IOC, FOK
    SelfTradePrevention,
    TriggerBy,

    # Market related
    MarketType,         # Spot, Perp
    FillType,
    KlineInterval,

    # Status related
    OrderStatus,
    DepositStatus,
    WithdrawalStatus,

    # And more...
)
```

## Examples

See the [examples](./examples) directory for complete usage examples:

- `example_public.py` - Public API examples
- `example_authenticated.py` - Authenticated API examples
- `example_websocket.py` - WebSocket streaming examples

## Documentation

For detailed API documentation, visit the [Backpack Exchange API Docs](https://docs.backpack.exchange/).

## Changelog

### v1.1.0
- Added 21 new API endpoints (RFQ, Strategy, Prediction Markets, etc.)
- Added 25+ new enum types
- Refactored SDK architecture using mixins
- 100% API coverage (70 endpoints)
- Full type hints support

### v1.0.x
- Initial release with basic API support

## Support

If this SDK has been helpful, please consider:

1. Using my referral link to register: [Register on Backpack Exchange](https://backpack.exchange/refer/solomeowl)
2. Giving this repo a star on GitHub

## License

MIT License
