from sqlalchemy import Column, Integer, String, Boolean,Date
from db.base_class import Base

class User(Base):
    id = Column(Integer,primary_key = True, index=True)
    username = Column(String, nullable=False)
    password = Column(String,nullable=False)
    role = Column(String,nullable=False)