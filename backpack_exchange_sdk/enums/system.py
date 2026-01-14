"""
System related enums for Backpack Exchange SDK.
"""

from enum import Enum


class SystemStatus(Enum):
    """System status."""
    OK = "Ok"
    MAINTENANCE = "Maintenance"


class SystemOrderType(Enum):
    """System order type."""
    COLLATERAL_CONVERSION = "CollateralConversion"
    FUTURE_EXPIRY = "FutureExpiry"
    LIQUIDATE_POSITION_ON_ADL = "LiquidatePositionOnAdl"
    LIQUIDATE_POSITION_ON_BOOK = "LiquidatePositionOnBook"
    LIQUIDATE_POSITION_ON_BACKSTOP = "LiquidatePositionOnBackstop"
    ORDER_BOOK_CLOSED = "OrderBookClosed"
