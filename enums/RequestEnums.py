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
