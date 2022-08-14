from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from infrastructure.models.transactionType import type_enum
from .user import  Username

class TransactionType(BaseModel):
    id: int
    name: str
    type: type_enum
    created_time: Optional[datetime] = None
    updated_time: Optional[datetime] = None
    created_user_id: Optional[int] = None
    updated_user_id: Optional[int] = None
    created_user: Optional[Username] = None
    class Config():
        orm_mode = True