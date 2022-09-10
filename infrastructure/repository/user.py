from infrastructure.models.user import User
from core.entity.user import User as UserDTO, PublicUser as PublicUserDTO
from fastapi.param_functions import Depends
from sqlalchemy.orm import Session
from infrastructure.session import get_db
from typing import List

class UserRepository:
    def __init__(self,db:Session=Depends(get_db)):
        self._db = db

    def list(self) -> List[PublicUserDTO]:
        users = self._db.query(User).order_by(User.id.desc()).all()
        return [PublicUserDTO.from_orm(user) for user in users]

    def getById(self,id: int) -> PublicUserDTO:
        user = self._db.query(User).get(id)
        return PublicUserDTO.from_orm(user)

    def persist(self,user) -> UserDTO:
        new_user = User(**user.dict())
        self._db.add(new_user)
        self._db.flush()
        self._db.refresh(new_user)
        return UserDTO.from_orm(new_user)

    def updateByUsername(self,username,data) -> None:
        user = self._db.query(User).filter(User.username == username)
        if type (data) is dict:
            user.update(data)
        else:
            user.update(data.dict())
        self._db.flush()
        return

    def update(self,id,data) -> None:
        user = self._db.query(User).filter(User.id == id)
        if type (data) is dict:
            user.update(data)
        else:
            user.update(data.dict())
        self._db.flush()
        return

    def readByUsername(self,username: str) -> UserDTO:
        user = self._db.query(User).filter(User.username == username).first()
        return UserDTO.from_orm(user)