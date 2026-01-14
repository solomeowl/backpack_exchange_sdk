"""
Strategy related enums for Backpack Exchange SDK.
"""

from enum import Enum


class StrategyTypeEnum(Enum):
    """Strategy type."""
    SCHEDULED = "Scheduled"


class StrategyStatus(Enum):
    """Strategy status."""
    RUNNING = "Running"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"
    TERMINATED = "Terminated"


class StrategyCrankCancelReason(Enum):
    """Reason for strategy cancellation."""
    EXPIRED = "Expired"
    FILL_OR_KILL = "FillOrKill"
    INSUFFICIENT_BORROWABLE_QUANTITY = "InsufficientBorrowableQuantity"
    INSUFFICIENT_FUNDS = "InsufficientFunds"
    INSUFFICIENT_LIQUIDITY = "InsufficientLiquidity"
    INVALID_PRICE = "InvalidPrice"
    INVALID_QUANTITY = "InvalidQuantity"
    INSUFFICIENT_MARGIN = "InsufficientMargin"
    LIQUIDATION = "Liquidation"
    MARKET_CLOSED = "MarketClosed"
    PRICE_OUT_OF_BOUNDS = "PriceOutOfBounds"
    REDUCE_ONLY = "ReduceOnly"
    UNKNOWN = "Unknown"
