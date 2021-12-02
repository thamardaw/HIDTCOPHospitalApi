from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from schemas.message import Message
from schemas.category import Category, showCategory
from db.repository import category
from db.session import get_db
from typing import List
from services.oauth2 import get_current_user
from schemas.token import TokenData

router = APIRouter(prefix="/category", tags=["Category"])

@router.get('/',status_code=status.HTTP_200_OK, response_model=List[showCategory])
def get_all_category(db: Session = Depends(get_db),current_user: TokenData = Depends(get_current_user)):
    return category.readAll(db)

@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=showCategory)
def get_category(id: int, db: Session = Depends(get_db),current_user: TokenData = Depends(get_current_user)):
    return category.read(id,db)

@router.post("/", status_code=status.HTTP_200_OK, response_model=Message)
def create(request: Category, db: Session = Depends(get_db),current_user: TokenData = Depends(get_current_user)):
    category.create(request, db,current_user)
    return {"detail": "Category create successful."}

@router.put("/{id}",status_code=status.HTTP_200_OK,response_model=Message)
def update(id: int, request: Category,db: Session = Depends(get_db),current_user: TokenData = Depends(get_current_user)):
    category.update(id,request,db,current_user)
    return {"detail": "Category update successful."}

@router.delete("/{id}",status_code=status.HTTP_200_OK, response_model=Message)
def delete(id: int, db: Session = Depends(get_db),current_user: TokenData = Depends(get_current_user)):
    category.delete(id,db)
    return {"detail": "Category delete successful."}