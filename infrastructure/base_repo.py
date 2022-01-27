from fastapi.param_functions import Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from infrastructure.base import  User
from .session import get_db
from utils.oauth2 import get_current_user
from exceptions.http import NOT_FOUND
from exceptions.repo import SQLALCHEMY_ERROR

class BaseRepo:
    def __init__(self,db:Session=Depends(get_db),user:User=Depends(get_current_user)):
        self._db = db
        self._user = user

    def readAll(self,model):
        try:
            return self._db.query(model).order_by(model.id.desc()).all()
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)

    def read(self,model,id) :
        try:
            data = self._db.query(model).get(id)
            if data is None:
                raise NOT_FOUND()
            return data
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)

    def create(self,model):
        try:
            model.create_stamp(self._user)
            self._db.add(model)
            self._db.flush()
            self._db.refresh(model)
            return model
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)

    def update(self,model,data:dict):
        try:
            for key,value in data.items():
                setattr(model,key,value)
            model.update_stamp(self._user)
            self._db.flush()
            return model
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)

    def delete(self,model,id) -> None:
        try:
            data = self._db.query(model).filter(model.id == id)
            data.delete(synchronize_session=False)
            self._db.flush()
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)