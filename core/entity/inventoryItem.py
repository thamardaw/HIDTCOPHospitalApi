from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date
from .pharmacyItem import PharmacyItem
from .salesServiceItem import SalesServiceItem
from .user import Username

class InventoryItem(BaseModel):
    id: int
    # pharmacy_item_id: Optional[int] = None
    # pharmacy_item: Optional[PharmacyItem] = None
    name: str
    balance: int
    unit: str
    purchasing_price: int
    sales_service_item_id: Optional[int] = None
    sales_service_item: Optional[SalesServiceItem] = None
    expiry_date: Optional[date] = None
    batch: str
    created_time: Optional[datetime] = None
    updated_time: Optional[datetime] = None
    created_user_id: Optional[int] = None
    updated_user_id: Optional[int] = None
    created_user: Optional[Username] = None
    class Config():
        orm_mode = True