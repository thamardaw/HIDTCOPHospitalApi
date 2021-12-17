from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from schemas.message import Message
from schemas.uom import Uom, showUom
from infrastructure.session import get_db
from infrastructure.repository.uom import UomRepository
from core.services.uom import UomService
from typing import List
from utils.oauth2 import extract_token_data
from schemas.token import TokenData

router = APIRouter(prefix="/uom", tags=["UOM"])

@router.get('/',status_code=status.HTTP_200_OK, response_model=List[showUom])
def get_all_uom(repo=Depends(UomRepository),tokenData: TokenData = Depends(extract_token_data)):
    return UomService(repo,tokenData).getAllUom()

@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=showUom)
def get_uom(id: int, repo=Depends(UomRepository),tokenData: TokenData = Depends(extract_token_data)):
    return UomService(repo,tokenData).getUom(id)

@router.post("/", status_code=status.HTTP_200_OK, response_model=Message)
def create(request: Uom, repo=Depends(UomRepository),tokenData: TokenData = Depends(extract_token_data)):
    UomService(repo,tokenData).addUom(request)
    return {"detail": "UOM create successful."}

@router.put("/{id}",status_code=status.HTTP_200_OK,response_model=Message)
def update(id: int, request: Uom,repo=Depends(UomRepository),tokenData: TokenData = Depends(extract_token_data)):
    UomService(repo,tokenData).updateUom(id,request)
    return {"detail": "UOM update successful."}

@router.delete("/{id}",status_code=status.HTTP_200_OK, response_model=Message)
def delete(id: int, repo=Depends(UomRepository),tokenData: TokenData = Depends(extract_token_data)):
    UomService(repo,tokenData).deleteUom(id)
    return {"detail": "UOM delete successful."}