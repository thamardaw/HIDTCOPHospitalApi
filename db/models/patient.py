import enum
from sqlalchemy import Column, Integer, String, Boolean, Date, Enum
from db.base_class import Base
import enum


class genderenum(enum.Enum):
    male = "male"
    female = "female"


class Patient(Base):
    patient_id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    genderenum = Column(Enum(genderenum))

    date_of_birth = Column(Date, nullable=False)
    age = Column(Integer, nullable=False)
    address = Column(String, nullable=False)
    contact_details = Column(String, nullable=False)
    blood_group = Column(String, nullable=False)
