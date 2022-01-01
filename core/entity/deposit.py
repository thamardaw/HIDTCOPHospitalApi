from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from .patient import Patient

class Deposit(BaseModel):
    id: int
    patient_id: int
    patient: Optional[Patient]
    amount: int
    remark: str
    created_time: Optional[datetime] = None
    updated_time: Optional[datetime] = None
    created_user_id: Optional[int] = None
    updated_user_id: Optional[int] = None
    class Config():
        orm_mode = True