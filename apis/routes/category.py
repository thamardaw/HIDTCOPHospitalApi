from fastapi import APIRouter, Depends, status
from schemas.message import Message
from schemas.category import Category
from schemas.bulkDelete import BulkDelete
from infrastructure.repository.salesServiceItem import SalesServiceItemRepository
from core.services.salesServiceItem import SalesServiceItemService
from core.entity.category import Category as CategoryDTO
from core.entity.category import CategorySmall as CategorySmallDTO

from typing import List
from fastapi_pagination import Page,Params,paginate

router = APIRouter(prefix="/category", tags=["Category"])

@router.get('/',status_code=status.HTTP_200_OK, response_model=List[CategorySmallDTO])
def get_all_category(repo=Depends(SalesServiceItemRepository)):
    return SalesServiceItemService(repo).getAllCategory()

@router.get('/p',status_code=status.HTTP_200_OK, response_model=Page[CategoryDTO])
def get_paginate_category(repo=Depends(SalesServiceItemRepository),params:Params=Depends()):
    return paginate(SalesServiceItemService(repo).getAllCategory(),params=params)

@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=CategoryDTO)
def get_category(id: int, repo=Depends(SalesServiceItemRepository)):
    return SalesServiceItemService(repo).getCategory(id)

@router.post("/", status_code=status.HTTP_200_OK, response_model=Message)
def create(request: Category, repo=Depends(SalesServiceItemRepository)):
    SalesServiceItemService(repo).createCategory(request)
    return {"detail": "Category create successful."}

@router.put("/{id}",status_code=status.HTTP_200_OK,response_model=Message)
def update(id: int, request: Category,repo=Depends(SalesServiceItemRepository)):
    SalesServiceItemService(repo).updateCategory(id,request)
    return {"detail": "Category update successful."}

@router.delete("/{id}",status_code=status.HTTP_200_OK, response_model=Message)
def delete(id: int, repo=Depends(SalesServiceItemRepository)):
    SalesServiceItemService(repo).deleteCategory(id)
    return {"detail": "Category delete successful."}

@router.post("/bulk",status_code=status.HTTP_200_OK, response_model=Message)
def bulk_delete(ids: BulkDelete, repo=Depends(SalesServiceItemRepository)):
    SalesServiceItemService(repo).deleteMulitpleCategory(ids)
    return {"detail": "Categories delete successful."}
