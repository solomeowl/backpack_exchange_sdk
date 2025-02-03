from backpack_exchange_sdk.websocket import WebSocketClient
import time
from datetime import datetime


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


def handle_depth(data):
    """Handle order book depth updates"""
    print("\n=== Depth Update ===")
    print(f"Symbol: {data['s']}")
    print("Asks:", data['a'])
    print("Bids:", data['b'])
    print(f"Update ID: {data['u']}")


def handle_mark_price(data):
    """Handle mark price updates"""
    print("\n=== Mark Price Update ===")
    print(f"Symbol: {data['s']}")
    print(f"Mark Price: {data['p']}")
    print(f"Funding Rate: {data['f']}")
    print(f"Index Price: {data['i']}")
    print(f"Next Funding: {datetime.fromtimestamp(data['n']/1000000).strftime('%Y-%m-%d %H:%M:%S')}")


def handle_ticker(data):
    """Handle 24hr ticker updates"""
    print("\n=== Ticker Update ===")
    print(f"Symbol: {data['s']}")
    print(f"Last Price: {data['c']}")
    print(f"24h High: {data['h']}")
    print(f"24h Low: {data['l']}")
    print(f"24h Volume: {data['v']}")


def handle_liquidation(data):
    """Handle liquidation events"""
    print("\n=== Liquidation Event ===")
    print(f"Symbol: {data['s']}")
    print(f"Price: {data['p']}")
    print(f"Quantity: {data['q']}")


def handle_order_update(data):
    """Handle order updates"""
    print("\n=== Order Update ===")
    print(f"Event Type: {data['e']}")
    print(f"Symbol: {data['s']}")
    print(f"Order ID: {data['i']}")
    print(f"Status: {data['X']}")
    if 'p' in data:
        print(f"Price: {data['p']}")
    if 'q' in data:
        print(f"Quantity: {data['q']}")


def handle_position_update(data):
    """Handle position updates"""
    print("\n=== Position Update ===")
    print(f"Event Type: {data.get('e', 'Initial')}")
    print(f"Symbol: {data['s']}")
    print(f"Position ID: {data['i']}")
    print(f"Quantity: {data['q']}")
    print(f"Entry Price: {data['B']}")
    print(f"Mark Price: {data['M']}")
    print(f"Unrealized PnL: {data['P']}")


def main():
    # Initialize WebSocket client
    ws_client = WebSocketClient(api_key="your_api_key", secret_key="your_secret_key")

    # Subscribe to public streams
    public_streams = [
        "bookTicker.SOL_USDC",      # Book ticker
        "trade.SOL_USDC",           # Trades
        "kline.1m.SOL_USDC",        # 1-minute kline
        "depth.SOL_USDC",           # Order book depth
        "markPrice.SOL_USDC",       # Mark price
        "ticker.SOL_USDC",          # 24hr ticker
        "liquidation"               # Liquidation events
    ]

    # Subscribe to private streams
    private_streams = [
        "account.orderUpdate.SOL_USDC",        # Order updates
        "account.positionUpdate.SOL_USDC"      # Position updates
    ]

    # Register handlers for different stream types
    stream_handlers = {
        "bookTicker.SOL_USDC": handle_book_ticker,
        "trade.SOL_USDC": handle_trades,
        "kline.1m.SOL_USDC": handle_kline,
        "depth.SOL_USDC": handle_depth,
        "markPrice.SOL_USDC": handle_mark_price,
        "ticker.SOL_USDC": handle_ticker,
        "liquidation": handle_liquidation
    }

    # Subscribe to public streams with their respective handlers
    for stream, handler in stream_handlers.items():
        ws_client.subscribe([stream], handler)

    # Subscribe to private streams
    ws_client.subscribe(
        ["account.orderUpdate.SOL_USDC"],
        handle_order_update,
        is_private=True
    )
    ws_client.subscribe(
        ["account.positionUpdate.SOL_USDC"],
        handle_position_update,
        is_private=True
    )

    print("WebSocket connection established")
    print("Press Ctrl+C to exit")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nClosing WebSocket connection...")
        ws_client.close()
        print("Program terminated")


if __name__ == "__main__":
    main()
