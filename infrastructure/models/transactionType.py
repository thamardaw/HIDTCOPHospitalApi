from sqlalchemy import Column, String, Enum
from infrastructure.base_mixin import BaseMixin
from infrastructure.base_class import Base
import enum

class type_enum(str, enum.Enum):
    issue = "issue"
    receive = "receive"

class TransactionType(BaseMixin,Base):
    name = Column(String,nullable=False)
    type = Column(Enum(type_enum),nullable=False)