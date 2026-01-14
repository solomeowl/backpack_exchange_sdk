"""
Borrow/Lend related enums for Backpack Exchange SDK.
"""

from enum import Enum


class BorrowLendBookState(Enum):
    """Borrow lend book state."""
    OPEN = "Open"
    CLOSED = "Closed"
    REPAY_ONLY = "RepayOnly"


class BorrowLendMarketHistoryInterval(Enum):
    """Borrow lend market history interval."""
    D1 = "1d"
    W1 = "1w"
    MONTH1 = "1month"
    YEAR1 = "1year"


class BorrowLendSource(Enum):
    """Source of borrow/lend operation."""
    ADL_PROVIDER = "AdlProvider"
    AUTO_BORROW_REPAY = "AutoBorrowRepay"
    AUTO_LEND = "AutoLend"
    BACKSTOP_PROVIDER = "BackstopProvider"
    DUST_CONVERSION = "DustConversion"
    INTEREST = "Interest"
    LIQUIDATION = "Liquidation"
    LIQUIDATION_ADL = "LiquidationAdl"
    LIQUIDATION_BACKSTOP = "LiquidationBackstop"
    MANUAL = "Manual"
    SETTLEMENT = "Settlement"
    WITHDRAWAL = "Withdrawal"
