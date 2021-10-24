from sqlalchemy.orm import Session
from fastapi import HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from db.models.user import User
from core import JWTtoken
from core.hashing import Hash

def authenticate(request:OAuth2PasswordRequestForm,db:Session):
    user = db.query(User).filter(User.username == request.username).first()
    if not user:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalid Credentials")
    if not Hash.verify_password(request.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Incorrect password")
    access_token = JWTtoken.create_access_token(
        data={"sub": user.username,"role":user.role}
    )
    return {"access_token": access_token, "token_type": "bearer","role":user.role}
