from db.models.user import User
from core.hashing import Hash
from sqlalchemy.orm import Session
from fastapi import HTTPException,status

def create(request:User,db:Session):
    if not request.username:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Username cannot be empty.")
    if len(request.password) < 6:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Password have to contain at least 6 character.")
    user = db.query(User).filter(User.username == request.username).first()
    if user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Username already exist.")
    new_user = User(username=request.username,password=Hash.hash_password(request.password),role=request.role)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user