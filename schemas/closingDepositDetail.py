from pydantic import BaseModel

class ClosingDepositDetail(BaseModel):
    deposit_id: int
    amount: int
