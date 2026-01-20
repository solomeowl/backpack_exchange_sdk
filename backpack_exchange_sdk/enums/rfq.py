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

