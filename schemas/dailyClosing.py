from pydantic import BaseModel
from typing import Optional, List
from .closingBillDetail import ClosingBillDetail
from .closingDepositDetail import ClosingDepositDetail

class DailyClosing(BaseModel):
    opening_balance: int
    closing_deposit_detail: Optional[List[ClosingDepositDetail]]
    closing_bill_detail : Optional[List[ClosingBillDetail]] 
    grand_total: int
    actual_amount: int 
    adjusted_amount: int 
    adjusted_reason: str
