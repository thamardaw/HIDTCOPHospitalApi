from pydantic import BaseModel
from typing import Optional
from infrastructure.models.transactionType import type_enum

class TransactionType(BaseModel):
    id: int
    name: str
    type: type_enum
    created_time: Optional[str] = None
    updated_time: Optional[str] = None
    created_user_id: Optional[int] = None
    updated_user_id: Optional[int] = None
    class Config():
        orm_mode = True