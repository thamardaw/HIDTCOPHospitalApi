from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from .uom import showUom
from .category import showCategory

class SalesServiceItem(BaseModel):
    name: str 
    price: int
    uom_id: int
    category_id: int

class showSalesServiceItem(BaseModel):
    id: int
    name: str 
    price: int
    uom_id: int
    uom: showUom
    category_id: int
    category: showCategory
    created_time: Optional[datetime] = None
    updated_time: Optional[datetime] = None
    created_user_id: Optional[int] = None
    updated_user_id: Optional[int] = None
    class Config():
        orm_mode = True