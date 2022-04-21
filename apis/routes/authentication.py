from fastapi import APIRouter, Depends
from schemas.token import Token, RefreshToken
from fastapi.security import OAuth2PasswordRequestForm
from infrastructure.repository.user import UserRepository
from core.services.user import UserService

router = APIRouter(tags=["Authentication"])

@router.post("/login",response_model=Token)
def login(request:OAuth2PasswordRequestForm = Depends(),repo=Depends(UserRepository)):
    return UserService(repo).authenticate(request)

@router.post("/refreshToken",response_model=Token)
def refresh_token(request:RefreshToken,repo=Depends(UserRepository)):
    return UserService(repo).refreshToken(request)