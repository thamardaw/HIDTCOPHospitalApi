from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from .user import ShowUser

class DailyClosing(BaseModel):
    id: int
    opening_balance: int
    deposit_total: int
    bill_total :int
    grand_total: int
    actual_amount: int 
    adjusted_amount: int 
    adjusted_reason: str
    created_time: Optional[datetime] = None
    updated_time: Optional[datetime] = None
    created_user_id: Optional[int] = None
    updated_user_id: Optional[int] = None
    created_user: Optional[ShowUser] = None
    class Config():
        orm_mode = True