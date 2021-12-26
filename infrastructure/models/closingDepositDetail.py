from sqlalchemy import Column, Integer
from infrastructure.base_mixin import BaseMixin
from sqlalchemy.sql.schema import ForeignKey
from infrastructure.base_class import Base
from sqlalchemy.orm import relationship

class ClosingDepositDetail(BaseMixin,Base):
    daily_closing_id = Column(Integer,ForeignKey("dailyclosing.id"))
    deposit_id = Column(Integer,ForeignKey("deposit.id"))
    deposit = relationship("Deposit",backref="closingdepositdetail")
    amount = Column(Integer)
    