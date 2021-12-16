from pydantic import BaseModel

class Payment(BaseModel):
    patient_id:int
    bill_id:int
    class Config():
        orm_mode = True