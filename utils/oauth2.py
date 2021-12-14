from fastapi import Depends

from fastapi import HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from .JWTtoken import verify_token,create_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    return verify_token(token)

def refreshToken(token:str):
    tokenData = verify_token(token)
    if tokenData.token_type == "access":
        raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    access_token = create_access_token(data={"sub": tokenData.username,"role":tokenData.role})
    return {"access_token": access_token, "token_type": "Bearer","refresh_token":token}

