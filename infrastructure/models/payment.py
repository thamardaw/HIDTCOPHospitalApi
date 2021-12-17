from sqlalchemy import Column, Integer
from infrastructure.base_mixin import BaseMixin
from sqlalchemy.sql.schema import ForeignKey
from infrastructure.base_class import Base

class Payment(BaseMixin,Base):
    patient_id = Column(Integer,ForeignKey("patient.id"))
    bill_id = Column(Integer,ForeignKey("bill.id"))
    total_amount = Column(Integer, nullable=False)
    total_deposit_amount = Column(Integer, nullable=False)
    collected_amount = Column(Integer, nullable=False)
    unpaid_amount = Column(Integer, nullable=False)