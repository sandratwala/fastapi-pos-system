from datetime import datetime

from pydantic import BaseModel, ConfigDict

class ReceiptCreate(BaseModel):
    sale_id: int
    receipt_number: str

class ReceiptRead(ReceiptCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime