from pydantic import BaseModel
from typing import Optional

class InventoryTransaction(BaseModel):
    inventory_item_id: int
    inventory_item_name: str
    transaction_type_name: str
    quantity: int
    unit: str
    purchasing_price: int
    selling_price: int
    note: Optional[str] = None