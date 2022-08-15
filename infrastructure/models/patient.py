from sqlalchemy import Column,  String, Date, Enum
from infrastructure.base_mixin import BaseMixin
from infrastructure.base_class import Base
import enum
from sqlalchemy.orm import relationship

class gender_enum(str, enum.Enum):
    male = "male"
    female = "female"

class Patient(BaseMixin,Base):
    name = Column(String, nullable=False)
    gender = Column(Enum(gender_enum))
    date_of_birth = Column(Date, nullable=True)
    age = Column(String, nullable=False)
    address = Column(String, nullable=False)
    contact_details = Column(String, nullable=False)
    
    bill = relationship("Bill",back_populates="patient")
    deposit = relationship("Deposit",back_populates="patient")
