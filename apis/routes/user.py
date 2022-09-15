from fastapi import APIRouter, Depends, status
from schemas.message import Message
from schemas.user import User, ResetPassword, UpdateUser
from infrastructure.repository.user import UserRepository
from core.services.user import UserService
from core.entity.user import PublicUser as PublicUserDTO
from utils.oauth2 import get_current_user
from typing import List

router = APIRouter(prefix="/user",tags=["User"])

@router.post("/",status_code=status.HTTP_200_OK,response_model=Message)
def create(request:User,repo=Depends(UserRepository)):
    UserService(repo).createUser(request)   
    return {"detail":"User create successful."}

@router.put("/resetPassword",status_code=status.HTTP_200_OK,response_model=Message)
def reset_password(request:ResetPassword,repo=Depends(UserRepository)):
    UserService(repo).resetPassword(request)
    return {"detail":"Password reset successful."}

@router.get("/",status_code=status.HTTP_200_OK,response_model=List[PublicUserDTO])
def get_all_users(repo=Depends(UserRepository),current_user:User=Depends(get_current_user)):
    return UserService(repo).getAllUser(current_user)

@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=PublicUserDTO)
def get_user(id: int, repo=Depends(UserRepository),current_user:User=Depends(get_current_user)):
    return UserService(repo).getUser(current_user,id)

@router.put("/{id}",status_code=status.HTTP_200_OK,response_model=Message)
def update_user(id: int,request:UpdateUser,repo=Depends(UserRepository),current_user:User=Depends(get_current_user)):
    UserService(repo).updateUser(current_user,id,request)
    return {"detail":"User update successful."}


