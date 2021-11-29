from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from schemas.message import Message
from schemas.salesServiceItem import SalesServiceItem,showSalesServiceItem
from db.repository import salesServiceItem
from db.session import get_db
from typing import List
from services.oauth2 import get_current_user
from schemas.user import User

router = APIRouter(prefix="/salesServiceItem", tags=["Sales Service Item"])

@router.get('/',status_code=status.HTTP_200_OK, response_model=List[showSalesServiceItem])
def get_all_sales_service_item(db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    return salesServiceItem.readAll(db)

@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=showSalesServiceItem)
def get_sales_service_item(id: int, db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    return salesServiceItem.read(id,db)

@router.post("/", status_code=status.HTTP_200_OK, response_model=Message)
def create(request: SalesServiceItem, db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    salesServiceItem.create(request, db,current_user)
    return {"detail": "Sales Service Item create successful."}

@router.put("/{id}",status_code=status.HTTP_200_OK,response_model=Message)
def update(id: int, request: SalesServiceItem,db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    salesServiceItem.update(id,request,db,current_user)
    return {"detail": "Sales Service Item update successful."}

@router.delete("/{id}",status_code=status.HTTP_200_OK, response_model=Message)
def delete(id: int, db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    salesServiceItem.delete(id,db)
    return {"detail": "Sales Service Item delete successful."}