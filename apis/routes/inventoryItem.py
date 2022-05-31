from typing import List
from fastapi import APIRouter, Depends, status
from schemas.message import Message
from schemas.bulkDelete import BulkDelete

from schemas.inventoryItem import InventoryItem
from core.entity.inventoryItem import InventoryItem as InventoryItemDTO

from core.services.inventory import InventoryService
from infrastructure.repository.inventory import InventoryRepository

router = APIRouter(prefix="/inventory_items", tags=["Inventory Items"])

@router.get('/',status_code=status.HTTP_200_OK, response_model=List[InventoryItemDTO])
def get_all_inventories(repo=Depends(InventoryRepository)):
    ls  = InventoryService(repo).getAllInventoryItem()
    return ls

@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=InventoryItemDTO)
def get_inventory(id: int, repo=Depends(InventoryRepository)):
    return InventoryService(repo).getInventoryItem(id)

@router.post("/", status_code=status.HTTP_200_OK, response_model=Message)
def create(request: InventoryItem, repo=Depends(InventoryRepository)):
    InventoryService(repo).createInventoryItem(request)
    return {"detail": "Inventory create successful."}

@router.put("/{id}",status_code=status.HTTP_200_OK,response_model=Message)
def update(id: int, request: InventoryItem,repo=Depends(InventoryRepository)):
    InventoryService(repo).updateInventoryItem(id,request)
    return {"detail": "Inventory update successful."}

@router.delete("/{id}",status_code=status.HTTP_200_OK, response_model=Message)
def delete(id: int, repo=Depends(InventoryRepository)):
    InventoryService(repo).deleteInventoryItem(id)
    return {"detail": "Inventory delete successful."}

@router.post("/bulk",status_code=status.HTTP_200_OK, response_model=Message)
def bulk_delete(ids: BulkDelete, repo=Depends(InventoryRepository)):
    InventoryService(repo).deleteMulitpleInventoryItem(ids)
    return {"detail": "Inventories delete successful."}