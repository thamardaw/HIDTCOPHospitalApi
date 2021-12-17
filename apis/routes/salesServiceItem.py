from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from schemas.message import Message
from schemas.salesServiceItem import SalesServiceItem,showSalesServiceItem
from infrastructure.repository import salesServiceItem
from infrastructure.session import get_db
from typing import List
from utils.oauth2 import extract_token_data
from schemas.token import TokenData

router = APIRouter(prefix="/salesServiceItem", tags=["Sales Service Item"])

@router.get('/',status_code=status.HTTP_200_OK, response_model=List[showSalesServiceItem])
def get_all_sales_service_item(db: Session = Depends(get_db),tokenData: TokenData = Depends(extract_token_data)):
    return salesServiceItem.readAll(db)

@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=showSalesServiceItem)
def get_sales_service_item(id: int, db: Session = Depends(get_db),tokenData: TokenData = Depends(extract_token_data)):
    return salesServiceItem.read(id,db)

@router.post("/", status_code=status.HTTP_200_OK, response_model=Message)
def create(request: SalesServiceItem, db: Session = Depends(get_db),tokenData: TokenData = Depends(extract_token_data)):
    salesServiceItem.create(request, db,tokenData)
    return {"detail": "Sales Service Item create successful."}

@router.post("/bulk", status_code=status.HTTP_200_OK, response_model=Message)
def bulk_create(request: List[SalesServiceItem], db: Session = Depends(get_db),tokenData: TokenData = Depends(extract_token_data)):
    salesServiceItem.bulkCreate(request, db,tokenData)
    return {"detail": "Sales Service Items create successful."}

@router.put("/{id}",status_code=status.HTTP_200_OK,response_model=Message)
def update(id: int, request: SalesServiceItem,db: Session = Depends(get_db),tokenData: TokenData = Depends(extract_token_data)):
    salesServiceItem.update(id,request,db,tokenData)
    return {"detail": "Sales Service Item update successful."}

@router.delete("/{id}",status_code=status.HTTP_200_OK, response_model=Message)
def delete(id: int, db: Session = Depends(get_db),tokenData: TokenData = Depends(extract_token_data)):
    salesServiceItem.delete(id,db)
    return {"detail": "Sales Service Item delete successful."}