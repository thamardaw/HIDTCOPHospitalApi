from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class BillItem(BaseModel):
    sales_service_item_id: int
    name: str
    quantity: int
    uom: str
    price: int
    remark: str

class showBillItem(BaseModel):
    id: int
    bill_id: int
    sales_service_item_id: int
    name: str
    quantity: int
    uom: str
    price: int
    subtotal: int
    remark: str
    created_time: Optional[datetime] = None
    updated_time: Optional[datetime] = None
    created_user_id: Optional[int] = None
    updated_user_id: Optional[int] = None
    class Config():
        orm_mode = True