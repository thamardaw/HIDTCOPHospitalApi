from infrastructure.base import User
from fastapi import HTTPException,status

def getCurrentUser(username,db_session):
    def func_decorator(func):
        def wrapped_func(*args,**kargs):
            user = db_session.query(User).filter(User.username == username).first()
            if not user:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User doesn't exist.")
            func(*args,user)
        return wrapped_func
    return func_decorator
