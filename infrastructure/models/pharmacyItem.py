from sqlalchemy import Column, Integer, String
from infrastructure.base_mixin import BaseMixin
from infrastructure.base_class import Base
from sqlalchemy.orm import relationship

class PharmacyItem(BaseMixin,Base):
    category_id = Column(Integer,nullable=False,index=True)
    brand_name = Column(String,nullable=False)
    generic_name = Column(String,nullable=False)
    form = Column(String)
    strength = Column(String)
    unit = Column(String,nullable=False)
    po_unit = Column(String)
    converstion_rate = Column(Integer)
    
    category = relationship('Category', primaryjoin="PharmacyItem.category_id==foreign(Category.id)",uselist=False)