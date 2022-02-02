from pydantic import BaseModel

class DepositUsed(BaseModel):
    deposit_id: int
    payment_id: int
    unpaid_amount: int
    deposit_amount: int

