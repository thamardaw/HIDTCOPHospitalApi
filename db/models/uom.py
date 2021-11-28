from sqlalchemy import Column,String
from db.base_mixin import BaseMixin
from db.base_class import Base
from sqlalchemy.orm import relationship

class Uom(BaseMixin,Base):
    name = Column(String, nullable=False)
    description = Column(String)
    sales_service_item = relationship("SalesServiceItem",back_populates="uom")