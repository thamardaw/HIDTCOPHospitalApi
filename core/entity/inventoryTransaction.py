from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from .inventoryItem import InventoryItem,InventoryItemSmall
from .user import Username

class InventoryTransaction(BaseModel):
    id: int
    inventory_item_id: Optional[int] = None
    inventory_item: Optional[InventoryItem] = None
    inventory_item_name: str
    transaction_type_name: str
    transaction_type: str
    quantity: int
    opening_balance: int
    closing_balance: int
    unit: str
    purchasing_price: int
    selling_price: int
    note: Optional[str] = None
    created_time: Optional[datetime] = None
    updated_time: Optional[datetime] = None
    created_user_id: Optional[int] = None
    updated_user_id: Optional[int] = None
    created_user: Optional[Username] = None
    
    class Config():
        orm_mode = True

class InventoryTransactionSmall(BaseModel):
    id: int
    inventory_item: Optional[InventoryItemSmall] = None
    transaction_type_name: str
    transaction_type: str
    quantity: int
    opening_balance: int
    closing_balance: int
    unit: str
    purchasing_price: int
    selling_price: int
    note: Optional[str] = None

    
    class Config():
        orm_mode = True
