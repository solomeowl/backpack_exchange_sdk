import json
import threading
import time
from typing import Callable, Dict, List, Optional

import websocket


class WebSocketClient:
    """
    WebSocket client for Backpack Exchange.
    Handles real-time data streams including market data, account updates, and trading information.
    """

    def __init__(self, api_key: str = None, secret_key: str = None):
        """
        Initialize WebSocket client.

        Args:
            api_key (str, optional): API key for authenticated streams
            secret_key (str, optional): Secret key for authenticated streams
        """
        self.ws = None
        self.api_key = api_key
        self.secret_key = secret_key
        self.base_url = "wss://ws.backpack.exchange"
        self.callbacks: Dict[str, List[Callable]] = {}
        self.connected = threading.Event()
        self.last_pong = time.time()
        self._connect()
        # Wait for connection to be established
        if not self.connected.wait(timeout=10):
            raise Exception("WebSocket connection timeout")

    def _connect(self):
        """
        Establish WebSocket connection and set up event handlers.
        Includes automatic reconnection on connection loss.
        """

        def on_message(ws, message):
            """Handle incoming WebSocket messages"""
            try:
                data = json.loads(message)
                stream = data.get("stream")
                if stream and stream in self.callbacks:
                    for callback in self.callbacks[stream]:
                        callback(data["data"])
            except Exception as e:
                print(f"Error processing message: {e}")

        def on_error(ws, error):
            """Handle WebSocket errors"""
            print(f"WebSocket error: {error}")
            self.connected.clear()

        def on_close(ws, close_status_code, close_msg):
            """
            Handle connection closure
            If server is shutting down (status 1001), wait 30s before reconnecting
            """
            print(f"WebSocket connection closed: {close_status_code} - {close_msg}")
            self.connected.clear()

            if close_status_code == 1001:  # Server shutting down
                print("Server shutting down, waiting 30s before reconnecting...")
                time.sleep(30)  # Wait for grace period
            else:
                time.sleep(5)  # Normal reconnection delay

            self._connect()

        def on_open(ws):
            """Handle WebSocket connection establishment"""
            print("WebSocket connection established")
            self.connected.set()

        def on_pong(ws, message):
            """Update last pong time"""
            self.last_pong = time.time()

        def on_ping(ws, message):
            """
            Handle ping from server by responding with pong immediately
            Server sends ping every 60s and expects pong within 120s
            """
            if hasattr(ws, "sock") and ws.sock:
                ws.sock.pong(message)

        # Initialize WebSocket connection with handlers
        self.ws = websocket.WebSocketApp(
            self.base_url,
            on_message=on_message,
            on_error=on_error,
            on_close=on_close,
            on_open=on_open,
            on_ping=on_ping,
            on_pong=on_pong,
        )

        # Start WebSocket connection in a separate thread
        # No need for ping_interval as server handles pinging
        wst = threading.Thread(target=self.ws.run_forever)
        wst.daemon = True
        wst.start()

    def _generate_signature(self, streams: List[str], timestamp: int, window: int = 5000) -> Dict[str, str]:
        """
        Generate authentication signature for private streams.

        Args:
            streams (List[str]): List of stream names to subscribe to
            timestamp (int): Current timestamp in milliseconds
            window (int): Signature validity window in milliseconds

        Returns:
            Dict[str, str]: Authentication headers
        """
        if not self.api_key or not self.secret_key:
            return {}

        sign_str = f"instruction=subscribe&timestamp={timestamp}&window={window}"
        signature = self._sign_message(sign_str)

        return {"api-key": self.api_key, "signature": signature, "timestamp": str(timestamp), "window": str(window)}

    def subscribe(self, streams: List[str], callback: Callable, is_private: bool = False):
        """
        Subscribe to one or more data streams.

        Args:
            streams (List[str]): List of stream names to subscribe to
            callback (Callable): Function to handle incoming messages
            is_private (bool): Whether these are private authenticated streams
        """
        # Wait for connection to be established
        if not self.connected.is_set():
            if not self.connected.wait(timeout=10):
                raise Exception("WebSocket connection not available")

        # Register callbacks for each stream
        for stream in streams:
            if stream not in self.callbacks:
                self.callbacks[stream] = []
            self.callbacks[stream].append(callback)

        # Prepare subscription message
        subscribe_data = {"method": "SUBSCRIBE", "params": streams}

        # Add authentication for private streams
        if is_private:
            timestamp = int(time.time() * 1000)
            auth_data = self._generate_signature(streams, timestamp)
            subscribe_data["signature"] = [
                auth_data["api-key"],
                auth_data["signature"],
                auth_data["timestamp"],
                auth_data["window"],
            ]

        # Send subscription request
        try:
            self.ws.send(json.dumps(subscribe_data))
        except Exception as e:
            print(f"Error subscribing to streams: {e}")
            raise

    def unsubscribe(self, streams: List[str]):
        """
        Unsubscribe from one or more data streams.

        Args:
            streams (List[str]): List of stream names to unsubscribe from
        """
        unsubscribe_data = {"method": "UNSUBSCRIBE", "params": streams}
        self.ws.send(json.dumps(unsubscribe_data))

        # Remove callbacks for unsubscribed streams
        for stream in streams:
            if stream in self.callbacks:
                del self.callbacks[stream]

    def close(self):
        """Gracefully close the WebSocket connection"""
        if self.ws:
            self.ws.close()
            self.connected.clear()
