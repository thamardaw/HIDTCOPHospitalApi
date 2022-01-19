from typing import List, Optional
from pydantic import BaseModel
from schemas.billItem import BillItem

class Bill(BaseModel):
    patient_id: int
    patient_name: str
    patient_phone: str
    patient_address: str
    bill_items: Optional[List[BillItem]] = []