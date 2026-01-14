"""
Utility functions for Backpack Exchange SDK.
"""

import base64
from typing import Dict, List, Optional, Any

from cryptography.hazmat.primitives.asymmetric import ed25519


def load_private_key(secret_key: str) -> ed25519.Ed25519PrivateKey:
    """
    Load an ED25519 private key from a base64-encoded string.

    Args:
        secret_key: Base64-encoded private key (seed)

    Returns:
        ED25519 private key object
    """
    return ed25519.Ed25519PrivateKey.from_private_bytes(base64.b64decode(secret_key))


def sign_message(private_key: ed25519.Ed25519PrivateKey, message: str) -> str:
    """
    Sign a message using an ED25519 private key.

    Args:
        private_key: ED25519 private key object
        message: Message to sign

    Returns:
        Base64-encoded signature
    """
    signature = private_key.sign(message.encode())
    return base64.b64encode(signature).decode()


def build_signing_string(
    instruction: str,
    params: Optional[Dict[str, Any]],
    timestamp: int,
    window: int
) -> str:
    """
    Build the signing string for an API request.

    Args:
        instruction: The API instruction (e.g., 'orderExecute', 'balanceQuery')
        params: Request parameters (query params or body)
        timestamp: Unix timestamp in milliseconds
        window: Request validity window in milliseconds

    Returns:
        The string to be signed
    """
    if params:
        # Normalize boolean values to lowercase strings
        normalized_params = {}
        for key, value in params.items():
            if isinstance(value, bool):
                normalized_params[key] = str(value).lower()
            else:
                normalized_params[key] = value

        # Sort parameters alphabetically and build query string
        param_str = "&" + "&".join(
            f"{k}={v}" for k, v in sorted(normalized_params.items())
        )
    else:
        param_str = ""

    return f"instruction={instruction}{param_str}&timestamp={timestamp}&window={window}"


def build_batch_signing_string(
    orders: List[Dict[str, Any]],
    timestamp: int,
    window: int
) -> str:
    """
    Build the signing string for batch order execution.

    For batch orders, each order needs its own instruction prefix,
    and they are concatenated together.

    Args:
        orders: List of order parameter dictionaries
        timestamp: Unix timestamp in milliseconds
        window: Request validity window in milliseconds

    Returns:
        The string to be signed for batch orders
    """
    order_strings = []

    for order in orders:
        # Normalize boolean values
        normalized_order = {}
        for key, value in order.items():
            if isinstance(value, bool):
                normalized_order[key] = str(value).lower()
            else:
                normalized_order[key] = value

        # Sort parameters alphabetically and build string with instruction prefix
        param_str = "&".join(
            f"{k}={v}" for k, v in sorted(normalized_order.items())
        )
        order_strings.append(f"instruction=orderExecute&{param_str}")

    # Concatenate all order strings and add timestamp/window
    return "&".join(order_strings) + f"&timestamp={timestamp}&window={window}"


def generate_auth_headers(
    public_key: str,
    private_key: ed25519.Ed25519PrivateKey,
    instruction: str,
    timestamp: int,
    window: int,
    params: Optional[Dict[str, Any]] = None
) -> Dict[str, str]:
    """
    Generate authentication headers for an API request.

    Args:
        public_key: Base64-encoded public key (API key)
        private_key: ED25519 private key object
        instruction: The API instruction
        timestamp: Unix timestamp in milliseconds
        window: Request validity window in milliseconds
        params: Optional request parameters

    Returns:
        Dictionary of authentication headers
    """
    sign_str = build_signing_string(instruction, params, timestamp, window)
    signature = sign_message(private_key, sign_str)

    return {
        "X-API-Key": public_key,
        "X-Signature": signature,
        "X-Timestamp": str(timestamp),
        "X-Window": str(window),
        "Content-Type": "application/json; charset=utf-8",
    }


def generate_batch_auth_headers(
    public_key: str,
    private_key: ed25519.Ed25519PrivateKey,
    orders: List[Dict[str, Any]],
    timestamp: int,
    window: int
) -> Dict[str, str]:
    """
    Generate authentication headers for batch order execution.

    Args:
        public_key: Base64-encoded public key (API key)
        private_key: ED25519 private key object
        orders: List of order parameter dictionaries
        timestamp: Unix timestamp in milliseconds
        window: Request validity window in milliseconds

    Returns:
        Dictionary of authentication headers
    """
    sign_str = build_batch_signing_string(orders, timestamp, window)
    signature = sign_message(private_key, sign_str)

    return {
        "X-API-Key": public_key,
        "X-Signature": signature,
        "X-Timestamp": str(timestamp),
        "X-Window": str(window),
        "Content-Type": "application/json; charset=utf-8",
    }


def generate_ws_signature(
    private_key: ed25519.Ed25519PrivateKey,
    timestamp: int,
    window: int = 5000
) -> str:
    """
    Generate signature for WebSocket authentication.

    Args:
        private_key: ED25519 private key object
        timestamp: Unix timestamp in milliseconds
        window: Request validity window in milliseconds

    Returns:
        Base64-encoded signature
    """
    sign_str = f"instruction=subscribe&timestamp={timestamp}&window={window}"
    return sign_message(private_key, sign_str)
