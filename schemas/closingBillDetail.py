from pydantic import BaseModel

class ClosingBillDetail(BaseModel):
    bill_id: int
    amount: int
