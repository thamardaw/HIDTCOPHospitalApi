from typing import List, Optional
from pydantic import BaseModel
from infrastructure.models.bill import printed_or_drafted_enum
from schemas.billItem import BillItem, showBillItem
from datetime import datetime

class Bill(BaseModel):
    patient_id: int
    bill_items: Optional[List[BillItem]] = []

class showBill(BaseModel):
    id: int
    patient_id:int
    patient_name: str
    patient_phone: str
    patient_age: int
    printed_or_drafted: printed_or_drafted_enum
    total_amount: int
    bill_items: Optional[List[showBillItem]] = []
    created_time: Optional[datetime] = None
    updated_time: Optional[datetime] = None
    created_user_id: Optional[int] = None
    updated_user_id: Optional[int] = None
    class Config():
        orm_mode = True