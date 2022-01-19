from sqlalchemy import Column,String
from infrastructure.base_mixin import BaseMixin
from infrastructure.base_class import Base
from sqlalchemy.orm import relationship

class Category(BaseMixin,Base):
    name = Column(String, nullable=False)
    description = Column(String)
    sales_service_item = relationship("SalesServiceItem",back_populates="category")