from sqlalchemy import Column, Integer,String, Boolean
from infrastructure.base_mixin import BaseMixin
from sqlalchemy.sql.schema import ForeignKey
from infrastructure.base_class import Base
from sqlalchemy.orm import relationship

class SalesServiceItem(BaseMixin,Base):
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    uom_id = Column(Integer,ForeignKey("uom.id"))
    uom = relationship("Uom",back_populates="sales_service_item")
    category_id = Column(Integer,ForeignKey("category.id"))
    is_active = Column(Boolean,nullable=False,server_default="true")
    
    category = relationship("Category",back_populates="sales_service_item")