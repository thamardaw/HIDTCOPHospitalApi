from typing import Optional
from pydantic import BaseModel

class Deposit(BaseModel):
    patient_id: int
    amount: int
    remark: Optional[str]
