from pydantic import BaseModel
from datetime import datetime
from typing import Optional,List
from .user import Username
from .deposit import Deposit
from .bill import Bill

class DailyClosing(BaseModel):
    id: int
    opening_balance: int
    deposit_total: int
    deposits: Optional[List[Deposit]] = []
    bill_total :int
    bills : Optional[List[Bill]] = []
    grand_total: int
    actual_amount: int 
    adjusted_amount: int 
    adjusted_reason: str
    created_time: Optional[datetime] = None
    updated_time: Optional[datetime] = None
    created_user_id: Optional[int] = None
    updated_user_id: Optional[int] = None
    created_user: Optional[Username] = None
<<<<<<< HEAD
=======
    class Config():
        orm_mode = True

class DailyClosingSmall(BaseModel):
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
    created_user: Optional[Username] = None
>>>>>>> 63d0fe93359fa2dc5ddfad31050b80fa8fff0ea5
    class Config():
        orm_mode = True 