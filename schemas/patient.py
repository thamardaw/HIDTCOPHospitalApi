from datetime import date
from pydantic import BaseModel
from infrastructure.models.patient import gender_enum

class Patient(BaseModel):
    name: str
    gender: gender_enum
    date_of_birth: date
    age: int
    address: str
    contact_details: str
