from fastapi import APIRouter, Depends, status
from schemas.message import Message
from schemas.category import Category
from infrastructure.repository.salesServiceItem import SalesServiceItemRepository
from core.services.salesServiceItem import SalesServiceItemService
from core.entity.category import Category as CategoryDTO
from typing import List

router = APIRouter(prefix="/category", tags=["Category"])

@router.get('/',status_code=status.HTTP_200_OK, response_model=List[CategoryDTO])
def get_all_category(repo=Depends(SalesServiceItemRepository)):
    return SalesServiceItemService(repo).getAllCategory()

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