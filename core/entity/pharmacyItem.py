from pydantic import BaseModel
from typing import Optional
from .category import Category
from datetime import datetime

class PharmacyItem(BaseModel):
    id: int
    category_id: Optional[int] = None
    category: Optional[Category] = None
    brand_name: str
    generic_name: str
    form: Optional[str] = None
    strength: Optional[str] = None
    unit: str
    po_unit: Optional[str] = None
    converstion_rate:  Optional[int] = None
    created_time: Optional[datetime] = None
    updated_time: Optional[datetime] = None
    created_user_id: Optional[int] = None
    updated_user_id: Optional[int] = None
    class Config():
        orm_mode = True