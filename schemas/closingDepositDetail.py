from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from .deposit import showDeposit

class ClosingDepositDetail(BaseModel):
    deposit_id: int
    amount: int

class showClosingDepositDetail(BaseModel):
    id: int
    daily_closing_id :int
    deposit_id: int
    deposit: showDeposit
    amount: int
    created_time: Optional[datetime] = None
    updated_time: Optional[datetime] = None
    created_user_id: Optional[int] = None
    updated_user_id: Optional[int] = None
    class Config():
        orm_mode = True