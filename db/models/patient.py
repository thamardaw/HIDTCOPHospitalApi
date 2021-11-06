from sqlalchemy import Column, Integer, String, Date, Enum
from db.base_mixin import BaseMixin
from db.base_class import Base
import enum

class gender_enum(str, enum.Enum):
    male = "male"
    female = "female"

class Patient(BaseMixin,Base):
    name = Column(String, nullable=False)
    gender = Column(Enum(gender_enum))
    date_of_birth = Column(Date, nullable=False)
    age = Column(Integer, nullable=False)
    address = Column(String, nullable=False)
    contact_details = Column(String, nullable=False)
