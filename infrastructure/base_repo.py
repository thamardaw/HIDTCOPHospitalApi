from sqlalchemy.orm import Session
from fastapi import Depends
from infrastructure.session import get_db
from core.entity.token import TokenData
from utils.oauth2 import extract_token_data
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException, status
from utils.getCurrentUser import getCurrentUser

SQLALCHEMY_ERROR = lambda exception,status_code = status.HTTP_500_INTERNAL_SERVER_ERROR: HTTPException(status_code=status_code,detail=str(exception.__dict__['orig']))
NOT_FOUND = HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Resource not found.')

class BaseRepo:
    def __init__(self,db:Session=Depends(get_db),tokenData:TokenData=Depends(extract_token_data)):
        self._db = db
        self._tokenData = tokenData

    def readAll(self,model):
        try:
            return self._db.query(model).all()
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)

    def read(self,model,id:int):
        try:
            data = self._db.query(model).get(id)
            if data is None:
                raise NOT_FOUND
            return data
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)

    def create(self,model):
        try:
            self._db.add(model)
            self._db.commit()
            self._db.refresh(model)
            return model
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)

    def update(self,model,data:dict):
        user = getCurrentUser(self._db,self._tokenData.username)
        data.update({"updated_user_id": user.id})
        try:
            for key,value in data.items():
                setattr(model,key,value)
            self._db.commit()
            return model
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)

    def delete(self,model) -> None:
        try:
            self._db.delete(model)
            self._db.commit()
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)