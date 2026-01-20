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
    PRICE_OUT_OF_BOUNDS = "PriceOutOfBounds"
    REDUCE_ONLY_NOT_REDUCED = "ReduceOnlyNotReduced"
    SELF_TRADE_PREVENTION = "SelfTradePrevention"
    UNKNOWN = "Unknown"
    USER_PERMISSIONS = "UserPermissions"


class SeriesRecurrence(Enum):
    """Series recurrence."""
    HOURLY = "hourly"
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    ANNUAL = "annual"
