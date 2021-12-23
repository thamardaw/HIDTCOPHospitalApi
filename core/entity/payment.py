from pydantic import BaseModel

class Payment(BaseModel):
    id: int
    bill_id: int
    total_amount: int
    total_deposit_amount: int
    collected_amount: int
    unpaid_amount: int
    is_outstanding: bool
    class Config():
        orm_mode = True