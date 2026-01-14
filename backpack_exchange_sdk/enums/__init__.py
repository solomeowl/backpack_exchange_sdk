"""
Enums for Backpack Exchange SDK.

This module provides all enum types used by the SDK.
"""

# Request enums (renamed from RequestEnums.py for PEP8 compliance)
from backpack_exchange_sdk.enums.request_enums import (
    TimeInForce,
    Side,
    SelfTradePrevention,
    OrderType,
    BorrowLendEventType,
    InterestPaymentSource,
    BorrowLendSide,
    BorrowLendPositionState,
    SettlementSourceFilter,
    TickerInterval,
    FillType,
    MarketType,
    OrderSide,
    CancelOrderType,
)

# Response enums (renamed from ResponseEnums.py for PEP8 compliance)
from backpack_exchange_sdk.enums.response_enums import Status

# Common enums
from backpack_exchange_sdk.enums.common import (
    Blockchain,
    SortDirection,
    TriggerBy,
)

# Market enums
from backpack_exchange_sdk.enums.market import (
    KlineInterval,
    KlinePriceType,
    DepthLimit,
    OrderBookState,
)

# Order enums
from backpack_exchange_sdk.enums.order import (
    OrderStatus,
    OrderExpiryReason,
)

# Capital enums
from backpack_exchange_sdk.enums.capital import (
    DepositStatus,
    WithdrawalStatus,
    DepositSource,
)

# Borrow/lend enums
from backpack_exchange_sdk.enums.borrow_lend import (
    BorrowLendBookState,
    BorrowLendMarketHistoryInterval,
    BorrowLendSource,
)

# RFQ enums
from backpack_exchange_sdk.enums.rfq import (
    RfqExecutionMode,
    RfqFillType,
    RfqStatus,
    QuoteStatus,
)

# Strategy enums
from backpack_exchange_sdk.enums.strategy import (
    StrategyTypeEnum,
    StrategyStatus,
    StrategyCrankCancelReason,
)

# Position enums
from backpack_exchange_sdk.enums.position import (
    PositionState,
    PaymentType,
)

# System enums
from backpack_exchange_sdk.enums.system import (
    SystemStatus,
    SystemOrderType,
)

# Error enums
from backpack_exchange_sdk.enums.errors import ApiErrorCode

__all__ = [
    # Request enums
    "TimeInForce",
    "Side",
    "SelfTradePrevention",
    "OrderType",
    "BorrowLendEventType",
    "InterestPaymentSource",
    "BorrowLendSide",
    "BorrowLendPositionState",
    "SettlementSourceFilter",
    "TickerInterval",
    "FillType",
    "MarketType",
    "OrderSide",
    "CancelOrderType",
    # Response enums
    "Status",
    # Common
    "Blockchain",
    "SortDirection",
    "TriggerBy",
    # Market
    "KlineInterval",
    "KlinePriceType",
    "DepthLimit",
    "OrderBookState",
    # Order
    "OrderStatus",
    "OrderExpiryReason",
    # Capital
    "DepositStatus",
    "WithdrawalStatus",
    "DepositSource",
    # Borrow/lend
    "BorrowLendBookState",
    "BorrowLendMarketHistoryInterval",
    "BorrowLendSource",
    # RFQ
    "RfqExecutionMode",
    "RfqFillType",
    "RfqStatus",
    "QuoteStatus",
    # Strategy
    "StrategyTypeEnum",
    "StrategyStatus",
    "StrategyCrankCancelReason",
    # Position
    "PositionState",
    "PaymentType",
    # System
    "SystemStatus",
    "SystemOrderType",
    # Errors
    "ApiErrorCode",
]
