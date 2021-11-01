from datetime import date
from typing import Any
from pydantic import BaseModel, Field
from db.models.patient import gender_enum

class Patient(BaseModel):
    name: str
    gender: gender_enum
    date_of_birth: date
    age: int
    address: str
    contact_details: str
    blood_group: str

class showPatient(BaseModel):
    id: int
    name: str
    gender: gender_enum
    date_of_birth: date
    age: int
    address: str
    contact_details: str
    blood_group: str
    class Config():
        orm_mode = True
