from db.models.user import User
from core.hashing import Hash
from sqlalchemy.orm import Session

def create(request:User,db:Session):
    new_user = User(username=request.username,password=Hash.hash_password(request.password),role=request.role)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user