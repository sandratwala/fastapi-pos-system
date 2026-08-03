from pydantic import BaseModel, ConfigDict
from decimal import Decimal
from datetime import datetime

class ProductBase(BaseModel):
    name: str
    sku: str
    price: Decimal
    category_id: int | None = None
    supplier_id: int | None = None
    is_active: bool = True

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: str | None = None
    sku: str | None = None
    price: Decimal | None = None
    category_id: int | None = None
    supplier_id: int | None = None
    is_active: bool | None = None

class ProductRead(ProductBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    created_at: datetime
