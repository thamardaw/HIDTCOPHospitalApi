from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class showPayment(BaseModel):
    id: int
    bill_id: int
    total_amount: int
    total_deposit_amount: int
    collected_amount: int
    unpaid_amount: int
    is_outstanding: bool
    created_time: Optional[datetime] = None
    updated_time: Optional[datetime] = None
    created_user_id: Optional[int] = None
    updated_user_id: Optional[int] = None
    class Config():
        orm_mode = True
