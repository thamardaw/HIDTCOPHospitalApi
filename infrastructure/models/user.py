from sqlalchemy import Column, String
from infrastructure.base_class import Base

class User(Base):
    username = Column(String, nullable=False)
    password = Column(String,nullable=False)
    role = Column(String,nullable=False)