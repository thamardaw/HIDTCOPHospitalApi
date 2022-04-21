from pydantic import BaseModel

class SalesServiceItem(BaseModel):
    name: str 
    price: int
    uom_id: int
    category_id: int