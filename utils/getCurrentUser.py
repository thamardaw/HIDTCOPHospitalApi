from infrastructure.base import User
from fastapi import HTTPException,status

def getCurrentUser(db_session,username):
    user = db_session.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User doesn't exist.")
    return user