from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.token import Token, RefreshToken
from fastapi.security import OAuth2PasswordRequestForm
from services.authentication import authenticate
from services.oauth2 import refreshToken

router = APIRouter(tags=["Authentication"])

@router.post("/login",response_model=Token)
def login(request:OAuth2PasswordRequestForm = Depends(),db:Session = Depends(get_db)):
    return authenticate(request,db)


@router.post("/refreshToken",response_model=Token)
def refresh_token(request:RefreshToken):
    return refreshToken(request.refresh_token)