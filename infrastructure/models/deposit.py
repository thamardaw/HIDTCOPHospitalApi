from sqlalchemy import Column, Integer,String
from infrastructure.base_mixin import BaseMixin
from sqlalchemy.sql.schema import ForeignKey
from infrastructure.base_class import Base

class Deposit(BaseMixin,Base):
    patient_id = Column(Integer,ForeignKey("patient.id"))
    amount = Column(Integer, nullable=False)
    remark = Column(String)