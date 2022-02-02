from typing import Optional
from datetime import timedelta,datetime
from exceptions.http import INVALID_CREDENTIAL
from config.config import settings
from jose import JWTError, jwt
from schemas.token import TokenData

class JWT:
    def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        to_encode.update({"token_type":"access"})
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        return encoded_jwt

    def create_refresh_token(data: dict, expires_delta: Optional[timedelta] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        to_encode.update({"token_type":"refresh"})
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        return encoded_jwt

    def verify_token(token:str) -> TokenData:
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
            username: str = payload.get("sub")
            role: str = payload.get("role")
            token_type : str = payload.get("token_type")
            if username is None or token_type is None or role is None:
                raise INVALID_CREDENTIAL
            return TokenData(username=username,token_type=token_type,role=role)
        except JWTError:
            raise INVALID_CREDENTIAL