from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from schemas.message import Message
from schemas.user import User
from db.session import get_db
from db.repository import user
from schemas.token import Token
from fastapi.security import OAuth2PasswordRequestForm
from services.authentication import authenticate

router = APIRouter(prefix="/user",tags=["User"])

@router.post("/",status_code=status.HTTP_200_OK,response_model=Message)
def create(request:User,db:Session = Depends(get_db)):
    user.create(request,db)
    return {"detail":"User create successful."}

@router.post("/login",response_model=Token)
def login(request:OAuth2PasswordRequestForm = Depends(),db:Session = Depends(get_db)):
    return authenticate(request,db)

# This route is for testing purpose and not a real route
# @router.get("/",status_code=status.HTTP_200_OK)
# def get(db:Session = Depends(get_db),current_user: User = Depends(get_current_user)):
#     return current_user