"""
Position related enums for Backpack Exchange SDK.
"""

from enum import Enum


class PositionState(Enum):
    """Position state."""
    OPEN = "Open"
    CLOSED = "Closed"


class PaymentType(Enum):
    """Payment type for interest calculations."""
    ENTRY_FEE = "EntryFee"
    BORROW = "Borrow"
    LEND = "Lend"
    UNREALIZED_POSITIVE_PNL = "UnrealizedPositivePnl"
    UNREALIZED_NEGATIVE_PNL = "UnrealizedNegativePnl"
