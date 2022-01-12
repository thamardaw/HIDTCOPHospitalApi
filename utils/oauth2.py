from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from .JWTtoken import JWT
from sqlalchemy.orm import Session
from infrastructure.session import get_db
from core.entity.user import User as UserDTO
from infrastructure.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")

def get_current_user(token: str = Depends(oauth2_scheme),db:Session=Depends(get_db)):
    payload = JWT.verify_token(token)
    user = db.query(User).filter(User.username == payload.username).first()
    return UserDTO.from_orm(user)