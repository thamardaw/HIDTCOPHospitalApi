from fastapi import APIRouter, Depends, status
from schemas.message import Message
from schemas.user import User, ResetPassword
from infrastructure.repository.user import UserRepository
from core.services.user import UserService

router = APIRouter(prefix="/user",tags=["User"])

@router.post("/",status_code=status.HTTP_200_OK,response_model=Message)
def create(request:User,repo=Depends(UserRepository)):
    UserService(repo).createUser(request)
    return {"detail":"User create successful."}

@router.put("/resetPassword",status_code=status.HTTP_200_OK,response_model=Message)
def reset_password(request:ResetPassword,repo=Depends(UserRepository)):
    UserService(repo).resetPassword(request)
    return {"detail":"Password reset successful."}
