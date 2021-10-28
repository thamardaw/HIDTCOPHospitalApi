from datetime import date
from typing import Any
from pydantic import BaseModel, Field
from enum import Enum


class gender_enum(str, Enum):
    male = "male"
    female = "female"


class Patients(BaseModel):
    name: str
    gender: gender_enum
    date_of_birth: date
    age: int
    address: str
    contact_details: str
    blood_group: str

class showPatient(BaseModel):
    name: str
    gender: Any
    date_of_birth: date
    age: int
    address: str
    contact_details: str
    blood_group: str
    class Config():
        orm_mode = True
