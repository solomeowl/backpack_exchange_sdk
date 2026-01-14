"""
RFQ (Request For Quote) related enums for Backpack Exchange SDK.
"""

from enum import Enum


class RfqExecutionMode(Enum):
    """RFQ execution mode."""
    AWAIT_ACCEPT = "AwaitAccept"
    IMMEDIATE = "Immediate"


class RfqFillType(Enum):
    """RFQ fill type filter."""
    USER = "User"
    COLLATERAL_CONVERSION = "CollateralConversion"


class RfqStatus(Enum):
    """RFQ status."""
    NEW = "New"
    FILLED = "Filled"
    CANCELLED = "Cancelled"
    EXPIRED = "Expired"


class QuoteStatus(Enum):
    """Quote status."""
    NEW = "New"
    FILLED = "Filled"
    CANCELLED = "Cancelled"
