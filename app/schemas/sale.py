from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict


class SaleBase(BaseModel):
    customer_id: Optional[int] = None
    subtotal: Decimal
    tax_amount: Decimal
    total_amount: Decimal
    user_id: int

class SaleCreate(SaleBase):
    pass

class SaleUpdate(BaseModel):
    customer_id: Optional[int] = None
    subtotal: Optional[Decimal] = None
    tax_amount: Optional[Decimal] = None
    total_amount: Optional[Decimal] = None

class SaleRead(SaleBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    sale_date: datetime