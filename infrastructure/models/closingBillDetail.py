from sqlalchemy import Column, Integer
from infrastructure.base_mixin import BaseMixin
from sqlalchemy.sql.schema import ForeignKey
from infrastructure.base_class import Base
from sqlalchemy.orm import relationship

class ClosingBillDetail(BaseMixin,Base):
    daily_closing_id = Column(Integer,ForeignKey("dailyclosing.id"))
    bill_id = Column(Integer,ForeignKey("bill.id"))
    bill = relationship("Bill",backref="closingbilldetail")
    amount = Column(Integer)
    