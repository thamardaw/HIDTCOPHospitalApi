from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from schemas.message import Message
from schemas.category import Category, showCategory
from infrastructure.repository import category
from infrastructure.session import get_db
from typing import List
from utils.oauth2 import extract_token_data
from schemas.token import TokenData

router = APIRouter(prefix="/category", tags=["Category"])

@router.get('/',status_code=status.HTTP_200_OK, response_model=List[showCategory])
def get_all_category(db: Session = Depends(get_db),tokenData: TokenData = Depends(extract_token_data)):
    return category.readAll(db)

@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=showCategory)
def get_category(id: int, db: Session = Depends(get_db),tokenData: TokenData = Depends(extract_token_data)):
    return category.read(id,db)

@router.post("/", status_code=status.HTTP_200_OK, response_model=Message)
def create(request: Category, db: Session = Depends(get_db),tokenData: TokenData = Depends(extract_token_data)):
    category.create(request, db,tokenData)
    return {"detail": "Category create successful."}

@router.put("/{id}",status_code=status.HTTP_200_OK,response_model=Message)
def update(id: int, request: Category,db: Session = Depends(get_db),tokenData: TokenData = Depends(extract_token_data)):
    category.update(id,request,db,tokenData)
    return {"detail": "Category update successful."}

@router.delete("/{id}",status_code=status.HTTP_200_OK, response_model=Message)
def delete(id: int, db: Session = Depends(get_db),tokenData: TokenData = Depends(extract_token_data)):
    category.delete(id,db)
    return {"detail": "Category delete successful."}