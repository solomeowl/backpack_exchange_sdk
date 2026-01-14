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
    MARKET_CLOSED = "MarketClosed"
    MAX_OPEN_ORDERS = "MaxOpenOrders"
    ORDER_BOOK_CLOSED = "OrderBookClosed"
    POSITION_LIMIT = "PositionLimit"
    POST_ONLY = "PostOnly"
    PRICE_BAND = "PriceBand"
    REDUCE_ONLY = "ReduceOnly"
    SELF_TRADE = "SelfTrade"
    STRATEGY_CANCEL = "StrategyCancel"
    TRIGGER_PRICE_BAND = "TriggerPriceBand"
    USER_CANCEL = "UserCancel"
