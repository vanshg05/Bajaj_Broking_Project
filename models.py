from enum import Enum

class OrderType(str, Enum):
    BUY = "BUY"
    SELL = "SELL"

class OrderStyle(str, Enum):
    MARKET = "MARKET"
    LIMIT = "LIMIT"

class OrderStatus(str, Enum):
    NEW = "NEW"
    PLACED = "PLACED"
    EXECUTED = "EXECUTED"
    CANCELLED = "CANCELLED"
