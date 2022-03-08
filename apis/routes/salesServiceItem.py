from fastapi import APIRouter, Depends, status
from schemas.message import Message
from schemas.bulkDelete import BulkDelete
from schemas.salesServiceItem import SalesServiceItem
from infrastructure.repository.salesServiceItem import SalesServiceItemRepository
from core.services.salesServiceItem import SalesServiceItemService
from core.entity.salesServiceItem import SalesServiceItem as SalesServiceItemDTO ,SalesServiceItemSmall as SalesServiceItemSmallDTO
from typing import List

router = APIRouter(prefix="/salesServiceItem", tags=["Sales & Service Item"])

@router.get('/',status_code=status.HTTP_200_OK, response_model=List[SalesServiceItemSmallDTO])
def get_all_sales_service_item(repo=Depends(SalesServiceItemRepository)):
    return SalesServiceItemService(repo).getAllSalesServiceItem()

@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=SalesServiceItemDTO)
def get_sales_service_item(id: int, repo=Depends(SalesServiceItemRepository)):
    return SalesServiceItemService(repo).getSalesServiceItem(id)

@router.post("/", status_code=status.HTTP_200_OK, response_model=Message)
def create(request: SalesServiceItem, repo=Depends(SalesServiceItemRepository)):
    SalesServiceItemService(repo).createSalesServiceItem(request)
    return {"detail": "Sales & Service Item create successful."}

@router.put("/{id}",status_code=status.HTTP_200_OK,response_model=Message)
def update(id: int, request: SalesServiceItem,repo=Depends(SalesServiceItemRepository)):
    SalesServiceItemService(repo).updateSalesServiceItem(id,request)
    return {"detail": "Sales & Service Item update successful."}

@router.delete("/{id}",status_code=status.HTTP_200_OK, response_model=Message)
def delete(id: int, repo=Depends(SalesServiceItemRepository)):
    SalesServiceItemService(repo).deleteSalesServiceItem(id)
    return {"detail": "Sales & Service Item delete successful."}

@router.post("/bulk",status_code=status.HTTP_200_OK, response_model=Message)
def bulk_delete(ids: BulkDelete, repo=Depends(SalesServiceItemRepository)):
    SalesServiceItemService(repo).deleteMulitpleSalesServiceItem(ids)
    return {"detail": "Sales Service Item delete successful."}