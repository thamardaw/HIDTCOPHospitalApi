from sqlalchemy import Column,String
from db.base_mixin import BaseMixin
from db.base_class import Base

class Uom(BaseMixin,Base):
    name = Column(String, nullable=False)
    description = Column(String)