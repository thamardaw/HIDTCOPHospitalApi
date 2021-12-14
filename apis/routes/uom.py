from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from schemas.message import Message
from schemas.uom import Uom, showUom
from infrastructure.repository import uom
from infrastructure.session import get_db
from typing import List
from utils.oauth2 import get_current_user
from schemas.token import TokenData

router = APIRouter(prefix="/uom", tags=["UOM"])

@router.get('/',status_code=status.HTTP_200_OK, response_model=List[showUom])
def get_all_uom(db: Session = Depends(get_db),current_user: TokenData = Depends(get_current_user)):
    return uom.readAll(db)

@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=showUom)
def get_uom(id: int, db: Session = Depends(get_db),current_user: TokenData = Depends(get_current_user)):
    return uom.read(id,db)

@router.post("/", status_code=status.HTTP_200_OK, response_model=Message)
def create(request: Uom, db: Session = Depends(get_db),current_user: TokenData = Depends(get_current_user)):
    uom.create(request, db,current_user)
    return {"detail": "UOM create successful."}

@router.put("/{id}",status_code=status.HTTP_200_OK,response_model=Message)
def update(id: int, request: Uom,db: Session = Depends(get_db),current_user: TokenData = Depends(get_current_user)):
    uom.update(id,request,db,current_user)
    return {"detail": "UOM update successful."}

@router.delete("/{id}",status_code=status.HTTP_200_OK, response_model=Message)
def delete(id: int, db: Session = Depends(get_db),current_user: TokenData = Depends(get_current_user)):
    uom.delete(id,db)
    return {"detail": "UOM delete successful."}