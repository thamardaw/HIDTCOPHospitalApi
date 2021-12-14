from sqlalchemy import Column, Integer
from infrastructure.base_mixin import BaseMixin
from sqlalchemy.sql.schema import ForeignKey
from infrastructure.base_class import Base

class DepositUsed(BaseMixin,Base):
    deposit_id = Column(Integer,ForeignKey("deposit.id"))
    payment_id = Column(Integer,ForeignKey("payment.id"))
    bill_id = Column(Integer, nullable=False)
    outstanding_amount_before = Column(Integer,nullable=False)
    outstanding_amount_after = Column(Integer, nullable=False)