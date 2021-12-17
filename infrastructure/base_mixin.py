from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import Column,Integer
from sqlalchemy.orm import relationship,declarative_mixin
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.sql.functions import func
from infrastructure.base import User

@declarative_mixin
class BaseMixin:
    created_time = Column(DateTime(timezone=True), server_default=func.now())
    updated_time = Column(DateTime(timezone=True), onupdate=func.now())
    @declared_attr
    def created_user_id(cls):
        return Column(Integer, ForeignKey('user.id'), default=0)
    @declared_attr
    def updated_user_id(cls):
        return Column(Integer, ForeignKey('user.id'), default=0)
    @declared_attr
    def created_user(cls):
        return relationship('User', primaryjoin=lambda: User.id==cls.created_user_id)
    @declared_attr
    def updated_user(cls):
        return relationship('User', primaryjoin=lambda: User.id==cls.updated_user_id)