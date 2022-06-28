from pydantic import BaseModel
from typing import Optional
from .inventoryItem import WithInventoryItem

class PharmacyItem(BaseModel):
    category_id : int
    brand_name : str
    generic_name : str
    form : Optional[str] = None
    strength : Optional[str] = None
    unit : str
    po_unit : Optional[str] = None
    converstion_rate : Optional[int] = None
    with_inventory: Optional[WithInventoryItem] = None