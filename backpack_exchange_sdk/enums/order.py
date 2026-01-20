"""
Order-related enums for Backpack Exchange SDK.
"""

from enum import Enum


class OrderStatus(Enum):
    """Order status."""
    CANCELLED = "Cancelled"
    EXPIRED = "Expired"
    FILLED = "Filled"
    NEW = "New"
    PARTIALLY_FILLED = "PartiallyFilled"
    TRIGGER_PENDING = "TriggerPending"
    TRIGGER_FAILED = "TriggerFailed"


class OrderExpiryReason(Enum):
    """Reason for order expiry."""
    ACCOUNT_TRADING_SUSPENDED = "AccountTradingSuspended"
    BORROW_REQUIRES_LEND_REDEEM = "BorrowRequiresLendRedeem"
    FILL_OR_KILL = "FillOrKill"
    INSUFFICIENT_BORROWABLE_QUANTITY = "InsufficientBorrowableQuantity"
    INSUFFICIENT_FUNDS = "InsufficientFunds"
    INSUFFICIENT_LIQUIDITY = "InsufficientLiquidity"
    INVALID_PRICE = "InvalidPrice"
    INVALID_QUANTITY = "InvalidQuantity"
    IMMEDIATE_OR_CANCEL = "ImmediateOrCancel"
    INSUFFICIENT_MARGIN = "InsufficientMargin"
    LIQUIDATION = "Liquidation"
    NEGATIVE_EQUITY = "NegativeEquity"
    POST_ONLY_MODE = "PostOnlyMode"
    POST_ONLY_TAKER = "PostOnlyTaker"
    PRICE_OUT_OF_BOUNDS = "PriceOutOfBounds"
    REDUCE_ONLY_NOT_REDUCED = "ReduceOnlyNotReduced"
    SELF_TRADE_PREVENTION = "SelfTradePrevention"
    STOP_WITHOUT_POSITION = "StopWithoutPosition"
    PRICE_IMPACT = "PriceImpact"
    UNKNOWN = "Unknown"
    USER_PERMISSIONS = "UserPermissions"
    MAX_STOP_ORDERS_PER_POSITION = "MaxStopOrdersPerPosition"
    POSITION_LIMIT = "PositionLimit"
    SLIPPAGE_TOLERANCE_EXCEEDED = "SlippageToleranceExceeded"
