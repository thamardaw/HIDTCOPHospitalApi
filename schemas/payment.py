from pydantic import BaseModel

class Payment(BaseModel):
    bill_id:int
