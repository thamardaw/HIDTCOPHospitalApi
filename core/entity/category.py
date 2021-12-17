from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Category(BaseModel):
    name: str
    description: str

class showCategory(BaseModel):
    id: int
    name: str
    description: str
    created_time: Optional[datetime] = None
    updated_time: Optional[datetime] = None
    created_user_id: Optional[int] = None
    updated_user_id: Optional[int] = None
    class Config():
        orm_mode = True