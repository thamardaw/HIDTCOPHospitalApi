from sqlalchemy import Column, Integer, String
from infrastructure.base_mixin import BaseMixin
from infrastructure.base_class import Base
from sqlalchemy.orm import relationship

class DailyClosing(BaseMixin,Base):
    opening_balance = Column(Integer, nullable=False)
    deposit_total = Column(Integer, nullable=False)
    bill_total = Column(Integer, nullable=False)
    grand_total = Column(Integer, nullable=False)
    actual_amount = Column(Integer, nullable=False)
    adjusted_amount = Column(Integer, nullable=False)
    adjusted_reason = Column(String, nullable=False)
    
    deposits = relationship("Deposit",secondary="closingdepositdetail",back_populates="dailyClosing")
    bills = relationship("Bill",secondary="closingbilldetail",back_populates="dailyClosing")