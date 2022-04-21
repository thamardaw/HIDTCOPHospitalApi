from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Category(BaseModel):
    id: int
    name: str
    description: str
    created_time: Optional[datetime] = None
    updated_time: Optional[datetime] = None
    created_user_id: Optional[int] = None
    updated_user_id: Optional[int] = None
    class Config():
        orm_mode = True

class CategorySmall(BaseModel):
    id: int
    name: str
    description: str
    class Config():
        orm_mode = True