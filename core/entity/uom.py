from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from .user import Username

class Uom(BaseModel):
    id: int
    name: str
    description: str
    created_time: Optional[datetime] = None
    updated_time: Optional[datetime] = None
    created_user_id: Optional[int] = None
    updated_user_id: Optional[int] = None
    created_user: Optional[Username] = None
    class Config():
        orm_mode = True

class UomSmall(BaseModel):
    id: int
    name: str
    description: str
    class Config():
        orm_mode = True