from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from .bill import Bill

class ClosingBillDetail(BaseModel):
    id: int
    daily_closing_id :int
    bill_id: int
    amount: int
    created_time: Optional[datetime] = None
    updated_time: Optional[datetime] = None
    created_user_id: Optional[int] = None
    updated_user_id: Optional[int] = None
    class Config():
        orm_mode = True

