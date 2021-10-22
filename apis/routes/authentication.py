from fastapi import APIRouter,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from db.session import get_db
from db.models.user import User
from core import JWTtoken
from core.hashing import Hash
from schemas.token import Token

router = APIRouter(tags=["Authentication"])

@router.post("/login",response_model=Token)
def login(request:OAuth2PasswordRequestForm = Depends(),db:Session = Depends(get_db)):
    user = db.query(User).filter(User.username == request.username).first()
    if not user:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalid Credentials")
    if not Hash.verify_password(request.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Incorrect password")
    access_token = JWTtoken.create_access_token(
        data={"sub": user.username,"role":user.role}
    )
    return {"access_token": access_token, "token_type": "bearer","role":user.role}