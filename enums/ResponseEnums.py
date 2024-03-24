from enum import Enum


class Status(Enum):
    """Statuses of json 'status' response"""
    CANCELLED = "Cancelled"
    EXPIRED = "Expired"
    FILLED = "Filled"
    NEW = "New"
    PARTIALLY_FILLED = "PartiallyFilled"
    TRIGGERED = "Triggered"
