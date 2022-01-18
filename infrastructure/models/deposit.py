from sqlalchemy import Column, Integer,String
from infrastructure.base_mixin import BaseMixin
from sqlalchemy.sql.schema import ForeignKey
from infrastructure.base_class import Base
from sqlalchemy.orm import relationship

class Deposit(BaseMixin,Base):
    patient_id = Column(Integer,ForeignKey("patient.id"))
    patient = relationship("Patient",backref="deposit")
    amount = Column(Integer, nullable=False)
    remark = Column(String)
    dailyClosing = relationship("DailyClosing",secondary="closingdepositdetail",back_populates="deposits")
