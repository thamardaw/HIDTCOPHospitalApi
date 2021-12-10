from sqlalchemy import Column, Integer
from db.base_mixin import BaseMixin
from sqlalchemy.sql.schema import ForeignKey
from db.base_class import Base

class Deposit(BaseMixin,Base):
    patient_id = Column(Integer,ForeignKey("patient.id"))
    amount = Column(Integer, nullable=False)