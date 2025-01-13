from enum import Enum


class TimeInForce(Enum):
    GTC = "GTC"
    IOC = "IOC"
    FOK = "FOK"


class Side(Enum):
    BID = "Bid"
    ASK = "Ask"


class SelfTradePrevention(Enum):
    REJECT_TAKER = "RejectTaker"
    REJECT_MAKER = "RejectMaker"
    REJECT_BOTH = "RejectBoth"
    ALLOW = "Allow"


class OrderType(Enum):
    MARKET = "Market"
    LIMIT = "Limit"


class BorrowLendEventType(Enum):
   BORROW = "Borrow"
   BORROW_REPAY = "BorrowRepay"
   LEND = "Lend"
   LEND_REDEEM = "LendRedeem"


class InterestPaymentSource(Enum):
    UNREALIZED_PNL = "UnrealizedPnl"
    BORROW_LEND = "BorrowLend"


class BorrowLendSide(Enum):
    BORROW = "Borrow"
    LEND = "Lend"


class BorrowLendPositionState(Enum):
    OPEN = "Open"
    CLOSED = "Closed"


class SettlementSourceFilter(Enum):
    BACKSTOP_LIQUIDATION = "BackstopLiquidation"
    CULLED_BORROW_INTEREST = "CulledBorrowInterest"
    CULLED_REALIZE_PNL = "CulledRealizePnl"
    CULLED_REALIZE_PNL_BOOK_UTILIZATION = "CulledRealizePnlBookUtilization"
    FUNDING_PAYMENT = "FundingPayment"
    REALIZE_PNL = "RealizePnl"
    TRADING_FEES = "TradingFees"
    TRADING_FEES_SYSTEM = "TradingFeesSystem"
