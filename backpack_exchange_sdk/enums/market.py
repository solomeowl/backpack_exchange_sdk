"""
Market-related enums for Backpack Exchange SDK.
"""

from enum import Enum


class KlineInterval(Enum):
    """K-line (candlestick) time intervals."""
    M1 = "1m"
    M3 = "3m"
    M5 = "5m"
    M15 = "15m"
    M30 = "30m"
    H1 = "1h"
    H2 = "2h"
    H4 = "4h"
    H6 = "6h"
    H8 = "8h"
    H12 = "12h"
    D1 = "1d"
    W1 = "1w"
    MONTH1 = "1month"


class KlinePriceType(Enum):
    """Price type for K-line data."""
    LAST = "Last"
    INDEX = "Index"
    MARK = "Mark"


class DepthLimit(Enum):
    """Depth limit for order book queries."""
    L5 = "5"
    L10 = "10"
    L20 = "20"
    L50 = "50"
    L100 = "100"
    L500 = "500"
    L1000 = "1000"


class OrderBookState(Enum):
    """Order book state."""
    OPEN = "Open"
    CLOSED = "Closed"
    CANCEL_ONLY = "CancelOnly"
    LIMIT_ONLY = "LimitOnly"
    POST_ONLY = "PostOnly"
