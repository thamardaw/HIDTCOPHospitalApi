from sqlalchemy import Column, Integer
from db.base_mixin import BaseMixin
from sqlalchemy.sql.schema import ForeignKey
from db.base_class import Base

class DepositUsed(BaseMixin,Base):
    deposit_id = Column(Integer,ForeignKey("deposit.id"))
    payment_id = Column(Integer,ForeignKey("payment.id"))
    bill_id = Column(Integer, nullable=False)
    outstanding_amount_before = Column(Integer,nullable=False)
    outstanding_amount_after = Column(Integer, nullable=False)