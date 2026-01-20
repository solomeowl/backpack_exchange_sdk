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
    CancelOrderType,
    SlippageToleranceType,
)

# Response enums (renamed from ResponseEnums.py for PEP8 compliance)
from backpack_exchange_sdk.enums.response_enums import Status

# Common enums
from backpack_exchange_sdk.enums.common import (
    Blockchain,
    SortDirection,
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
    FiatAsset,
    EqualsMoneyWithdrawalState,
    SettlementSource,
    CustodyAsset,
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
)

# Strategy enums
from backpack_exchange_sdk.enums.strategy import (
    StrategyTypeEnum,
    StrategyStatus,
    StrategyCrankCancelReason,
    SeriesRecurrence,
)

# Position enums
from backpack_exchange_sdk.enums.position import (
    PositionState,
    PaymentType,
)

# System enums
from backpack_exchange_sdk.enums.system import (
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
    "CancelOrderType",
    "SlippageToleranceType",
    # Response enums
    "Status",
    # Common
    "Blockchain",
    "SortDirection",
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
    "FiatAsset",
    "EqualsMoneyWithdrawalState",
    "SettlementSource",
    "CustodyAsset",
    # Borrow/lend
    "BorrowLendBookState",
    "BorrowLendMarketHistoryInterval",
    "BorrowLendSource",
    # RFQ
    "RfqExecutionMode",
    "RfqFillType",
    # Strategy
    "StrategyTypeEnum",
    "StrategyStatus",
    "StrategyCrankCancelReason",
    "SeriesRecurrence",
    # Position
    "PositionState",
    "PaymentType",
    # System
    "SystemOrderType",
    # Errors
    "ApiErrorCode",
]
