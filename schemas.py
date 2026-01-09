from pydantic import BaseModel
from typing import Optional
from models import OrderType, OrderStyle

class OrderRequest(BaseModel):
    symbol: str
    quantity: int
    orderType: OrderType
    orderStyle: OrderStyle
    price: Optional[float] = None
