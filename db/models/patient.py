from sqlalchemy import Column, Integer, String, Date, Enum
from db.base_model import BaseModel
import enum

class gender_enum(str, enum.Enum):
    male = "male"
    female = "female"

class Patient(BaseModel):
    name = Column(String, nullable=False)
    gender = Column(Enum(gender_enum))
    date_of_birth = Column(Date, nullable=False)
    age = Column(Integer, nullable=False)
    address = Column(String, nullable=False)
    contact_details = Column(String, nullable=False)
    blood_group = Column(String, nullable=False)
