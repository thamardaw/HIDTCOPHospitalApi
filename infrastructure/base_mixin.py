from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import Column,Integer
from sqlalchemy.orm import relationship, declarative_mixin, foreign
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.sql.functions import func
from infrastructure.base import User

@declarative_mixin
class BaseMixin:
    created_time = Column(DateTime(timezone=True), server_default=func.now())
    updated_time = Column(DateTime(timezone=True), onupdate=func.now())
    @declared_attr
    def created_user_id(cls):
        return Column(Integer,index=True)
    @declared_attr
    def updated_user_id(cls):
        return Column(Integer,index=True)
    @declared_attr
    def created_user(cls):
        return relationship('User', primaryjoin=lambda: User.id==foreign(cls.created_user_id),uselist=False)
    @declared_attr
    def updated_user(cls):
        return relationship('User', primaryjoin=lambda: User.id==foreign(cls.updated_user_id),uselist=False)

    def create_stamp(self, user:User):
        self.created_user_id = user.id
        self.updated_user_id = user.id

    def update_stamp(self, user:User):
        self.updated_user_id = user.id