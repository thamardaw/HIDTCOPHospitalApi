from sqlalchemy import Column, Integer, String
from infrastructure.base_mixin import BaseMixin
from sqlalchemy.sql.schema import ForeignKey
from infrastructure.base_class import Base
from sqlalchemy.orm import relationship

class PharmacyItem(BaseMixin,Base):
    category_id = Column(Integer,ForeignKey("category.id"))
    category = relationship("Category",backref="pharmacyitem")
    brand_name = Column(String,nullable=False)
    generic_name = Column(String,nullable=False)
    form = Column(String)
    strength = Column(String)
    unit = Column(String,nullable=False)
    po_unit = Column(String)
    converstion_rate = Column(Integer)