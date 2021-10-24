from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from schemas.message import Message
from schemas.user import User
from db.session import get_db
from db.repository import user
from core.oauth2 import get_current_user

router = APIRouter(prefix="/user",tags=["User"])

@router.post("/",status_code=status.HTTP_200_OK,response_model=Message)
def create(request:User,db:Session = Depends(get_db)):
    user.create(request,db)
    return {"detail":"User create successful."}

# This route is for testing purpose and not a real route
# @router.get("/",status_code=status.HTTP_200_OK)
# def get(db:Session = Depends(get_db),current_user: User = Depends(get_current_user)):
#     return current_user