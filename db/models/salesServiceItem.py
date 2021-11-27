from sqlalchemy import Column, Integer,String
from db.base_mixin import BaseMixin
from sqlalchemy.sql.schema import ForeignKey
from db.base_class import Base

class SalesServiceItem(BaseMixin,Base):
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    uom_id = Column(Integer,ForeignKey("uom.id"))
    category_id = Column(Integer,ForeignKey("category.id"))