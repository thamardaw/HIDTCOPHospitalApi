from typing import List, Optional
from pydantic import BaseModel
from infrastructure.models.bill import printed_or_drafted_enum
from core.entity.billItem import BillItem
from datetime import datetime
from .patient import Patient
from .payment import Payment

class Bill(BaseModel):
    id: int
    patient_id:int
    patient: Optional[Patient]
    patient_name: str
    patient_phone: str
    patient_address: str
    printed_or_drafted: printed_or_drafted_enum
    total_amount: int
    payment: Optional[List[Payment]]
    bill_items: Optional[List[BillItem]] = []
    created_time: Optional[datetime] = None
    updated_time: Optional[datetime] = None
    created_user_id: Optional[int] = None
    updated_user_id: Optional[int] = None
    class Config():
        orm_mode = True