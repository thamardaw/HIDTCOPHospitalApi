from sqlalchemy import Column, Integer,String, Boolean
from infrastructure.base_mixin import BaseMixin
from sqlalchemy.sql.schema import ForeignKey
from infrastructure.base_class import Base
from sqlalchemy.orm import relationship

class Deposit(BaseMixin,Base):
    patient_id = Column(Integer,ForeignKey("patient.id"))
    patient = relationship("Patient",backref="deposit")
    amount = Column(Integer, nullable=False)
    remark = Column(String)
    is_cancelled = Column(Boolean,nullable=False,server_default="false")
    dailyClosing = relationship("DailyClosing",secondary="closingdepositdetail",back_populates="deposits")
