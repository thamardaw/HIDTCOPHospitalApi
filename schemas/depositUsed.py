from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class DepositUsed(BaseModel):
    deposit_id: int
    payment_id: int
    unpaid_amount: int
    deposit_amount: int

class showDepositUsed(BaseModel):
    id: int
    deposit_id: int
    payment_id: int
    unpaid_amount: int
    deposit_amount: int
    created_time: Optional[datetime] = None
    updated_time: Optional[datetime] = None
    created_user_id: Optional[int] = None
    updated_user_id: Optional[int] = None
    class Config():
        orm_mode = True
