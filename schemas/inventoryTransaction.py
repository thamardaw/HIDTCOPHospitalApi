from pydantic import BaseModel
from typing import Optional
from infrastructure.models.transactionType import type_enum

class InventoryTransaction(BaseModel):
    inventory_item_id: int
    inventory_item_name: str
    transaction_type_name: str
    transaction_type: type_enum
    quantity: int
    unit: str
    purchasing_price: int
    selling_price: int
    note: Optional[str] = None