from fastapi import APIRouter, Depends, status
from schemas.message import Message
from schemas.uom import Uom
from schemas.bulkDelete import BulkDelete
from infrastructure.repository.salesServiceItem import SalesServiceItemRepository
from core.services.salesServiceItem import SalesServiceItemService
from core.entity.uom import Uom as UomDTO
from typing import List

router = APIRouter(prefix="/uom", tags=["UOM"])

@router.get('/',status_code=status.HTTP_200_OK, response_model=List[UomDTO])
def get_all_uom(repo=Depends(SalesServiceItemRepository)):
    return SalesServiceItemService(repo).getAllUom()

@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=UomDTO)
def get_uom(id: int, repo=Depends(SalesServiceItemRepository)):
    return SalesServiceItemService(repo).getUom(id)

@router.post("/", status_code=status.HTTP_200_OK, response_model=Message)
def create(request: Uom, repo=Depends(SalesServiceItemRepository)):
    SalesServiceItemService(repo).createUom(request)
    return {"detail": "UOM create successful."}

@router.put("/{id}",status_code=status.HTTP_200_OK,response_model=Message)
def update(id: int, request: Uom,repo=Depends(SalesServiceItemRepository)):
    SalesServiceItemService(repo).updateUom(id,request)
    return {"detail": "UOM update successful."}

@router.delete("/{id}",status_code=status.HTTP_200_OK, response_model=Message)
def delete(id: int, repo=Depends(SalesServiceItemRepository)):
    SalesServiceItemService(repo).deleteUom(id)
    return {"detail": "UOM delete successful."}

@router.post("/bulk",status_code=status.HTTP_200_OK, response_model=Message)
def bulk_delete(ids: BulkDelete, repo=Depends(SalesServiceItemRepository)):
    SalesServiceItemService(repo).deleteMulitpleUom(ids)
    return {"detail": "UOMs delete successful."}
