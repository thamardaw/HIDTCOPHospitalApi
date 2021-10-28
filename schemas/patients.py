

from datetime import date
from pydantic import BaseModel, Field
from enum import Enum


class gender_enum(str, Enum):
    male = "male"
    female = "female"


class Patients(BaseModel):
    patient_id: int
    name: str
    genderenum: gender_enum

    date_of_birth: date
    age: int
    address: str
    contact_details: str
    blood_group: str


# class PatientsEntry(BaseModel):
#     patient_id: int
#     name: str = Field(..., example="john")
#     genderenum: gender_enum = Field(..., example="male")

#     date_of_birth: date = Field(...)
#     age: int = Field(..., example="20")
#     address: str = Field(...)
#     contact_details: str = Field(...)
#     blood_group: str = Field(..., example="O")


# class PatientsUpdate(BaseModel):
#     patient_id: int
#     name: str = Field(..., example="john")
#     genderenum: gender_enum = Field(..., example="male")

#     date_of_birth: date = Field(...)
#     age: int = Field(..., example="20")
#     address: str = Field(...)
#     contact_details: str = Field(...)
#     blood_group: str = Field(..., example="O")


# class PatientsDelete(BaseModel):
#     patient_id: int = Field(..., example="Enter your id")
