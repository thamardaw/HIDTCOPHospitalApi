from sqlalchemy import Column, Integer, String, Enum
from infrastructure.base_mixin import BaseMixin
from sqlalchemy.sql.schema import ForeignKey
from infrastructure.base_class import Base
from sqlalchemy.orm import relationship
import enum

class printed_or_drafted_enum(str,enum.Enum):
    printed = "printed"
    drafted = "drafted"

class Bill(BaseMixin,Base):
    patient_id = Column(Integer,ForeignKey("patient.id"))
    patient = relationship("Patient",backref="bill")
    patient_name = Column(String, nullable=False)
    patient_phone = Column(String, nullable=False)
    patient_address = Column(String, nullable=False)
    printed_or_drafted = Column(Enum(printed_or_drafted_enum))
    total_amount = Column(Integer, nullable=False)
    bill_items = relationship("BillItem",back_populates="bill")
    payment = relationship("Payment",back_populates="bill")