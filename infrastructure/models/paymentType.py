from sqlalchemy import Column, String,Boolean
from infrastructure.base_mixin import BaseMixin
from infrastructure.base_class import Base

class PaymentType(BaseMixin,Base):
    name = Column(String,nullable=False)
    is_default = Column(Boolean)
