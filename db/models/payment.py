from sqlalchemy import Column, Integer
from db.base_mixin import BaseMixin
from sqlalchemy.sql.schema import ForeignKey
from db.base_class import Base

class Payment(BaseMixin,Base):
    patient_id = Column(Integer,ForeignKey("patient.id"))
    bill_id = Column(Integer,ForeignKey("bill.id"))
    total_amount = Column(Integer, nullable=False)
    total_deposit_amount = Column(Integer, nullable=False)
    collected_amount = Column(Integer, nullable=False)
    total_outstanding_amount = Column(Integer, nullable=False)