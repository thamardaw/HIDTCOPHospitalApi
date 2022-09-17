from pydantic import BaseModel

class PaymentType(BaseModel):
    name:str
    is_default:bool