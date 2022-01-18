from sqlalchemy import Column, Integer
from infrastructure.base_mixin import BaseMixin
from sqlalchemy.sql.schema import ForeignKey
from infrastructure.base_class import Base

class ClosingBillDetail(BaseMixin,Base):
    daily_closing_id = Column(Integer,ForeignKey("dailyclosing.id"))
    bill_id = Column(Integer,ForeignKey("bill.id"))
    amount = Column(Integer)
    