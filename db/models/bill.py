from sqlalchemy import Column, Integer, String
from db.base_mixin import BaseMixin
from sqlalchemy.sql.schema import ForeignKey
from db.base_class import Base

class Bill(BaseMixin,Base):
    patient_id = Column(Integer,ForeignKey("patient.id"))
    patient_name = Column(String, nullable=False)
    patient_phone = Column(String, nullable=False)
    patient_age = Column(String, nullable=False)
    total_amount = Column(Integer, nullable=False)