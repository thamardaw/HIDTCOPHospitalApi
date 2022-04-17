from pydantic import BaseModel
from typing import Optional
from datetime import datetime
<<<<<<< HEAD
from .uom import Uom
from .category import Category
=======
from .uom import Uom, UomSmall
from .category import Category, CategorySmall
>>>>>>> 63d0fe93359fa2dc5ddfad31050b80fa8fff0ea5

class SalesServiceItem(BaseModel):
    id: int
    name: str 
    price: int
    uom_id: Optional[int]
    uom: Optional[Uom]
    category_id: int
    category: Category
    created_time: Optional[datetime] = None
    updated_time: Optional[datetime] = None
    created_user_id: Optional[int] = None
    updated_user_id: Optional[int] = None
    class Config():
        orm_mode = True

class SalesServiceItemSmall(BaseModel):
    id: int
    name: str 
    price: int
    uom: Optional[UomSmall]
    category: CategorySmall
    class Config():
        orm_mode = True