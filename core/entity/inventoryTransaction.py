from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from .inventoryItem import InventoryItem

class InventoryTransaction(BaseModel):
    id: int
    inventory_item_id: Optional[int] = None
    inventory_item: Optional[InventoryItem] = None
    inventory_item_name: str
    transaction_type_name: str
    quantity: int
    opening_balance: int
    closing_balance: int
    unit: str
    purchasing_price: int
    selling_price: int
    note: str
    created_time: Optional[datetime] = None
    updated_time: Optional[datetime] = None
    created_user_id: Optional[int] = None
    updated_user_id: Optional[int] = None
    class Config():
        orm_mode = True
