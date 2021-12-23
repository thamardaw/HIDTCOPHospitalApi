from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Deposit(BaseModel):
    id: int
    patient_id: int
    amount: int
    created_time: Optional[datetime] = None
    updated_time: Optional[datetime] = None
    created_user_id: Optional[int] = None
    updated_user_id: Optional[int] = None
    class Config():
        orm_mode = True