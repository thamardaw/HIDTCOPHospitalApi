from pydantic import BaseModel

class BillItem(BaseModel):
    sales_service_item_id: int
    name: str
    quantity: int
    uom: str
    price: int
    remark: str

class InvBillItem(BaseModel):
    id: int
    bill_id: int
    sales_service_item_id: int
    name: str
    quantity: int
    uom: str
    price: int
    subtotal: int
    remark: str