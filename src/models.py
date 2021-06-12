from enum import Enum
from typing import Optional
from pydantic import BaseModel


class SideEnum(str, Enum):
    buy = "buy"
    sell = "sell"


class Trade(BaseModel):
    price: float
    size: float
    side: SideEnum
    symbol: str
    password: str
    type: str
    stop: Optional[str]
    stop_price: Optional[float]
    close_opposite_orders: bool  # true will cancel all open opposite orders


class Password(BaseModel):
    password: str