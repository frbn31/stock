from sqlmodel import Field, SQLModel
from typing import Optional, Any, Self, Type

class StockLocation(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

class StockMove(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    product: str
    quantity: float


