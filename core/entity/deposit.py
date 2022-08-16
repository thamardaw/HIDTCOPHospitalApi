from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from .patient import Patient
from .user import Username 

class Deposit(BaseModel):
    id: int
    patient_id: int
    patient: Optional[Patient]
    amount: int
    remark: str
    is_cancelled : bool
    created_time: Optional[datetime] = None
    updated_time: Optional[datetime] = None
    created_user_id: Optional[int] = None
    updated_user_id: Optional[int] = None
    created_user: Optional[Username] = None
    class Config():
        orm_mode = True