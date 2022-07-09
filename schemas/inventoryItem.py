from datetime import date
from pydantic import BaseModel
from typing import Optional

class InventoryItem(BaseModel):
    # pharmacy_item_id: int
    name: str
    balance: int
    unit: str
    purchasing_price: int
    sales_service_item_id: Optional[int] = None
    expiry_date: Optional[date] = None
    batch: str
    
class WithInventoryItem(BaseModel):
    name: str
    balance: int
    unit: str
    purchasing_price: int
    sales_service_item_id: int
    expiry_date: Optional[date] = None
    batch: str