from typing import List
from fastapi import APIRouter, Depends, status
from schemas.message import Message
from schemas.bulkDelete import BulkDelete

from schemas.inventoryTransaction import InventoryTransaction
from core.entity.inventoryTransaction import InventoryTransaction as InventoryTransactionDTO
# Call Service and Repo from Inventory
from core.services.inventory import InventoryService
from infrastructure.repository.inventory import InventoryRepository

router = APIRouter(prefix="/inventory_transactions", tags=["InventoryTransactions"])

@router.get('/', status_code=status.HTTP_200_OK, response_model=List[InventoryTransactionDTO])
def get_all_inventory_transactions(repo=Depends(InventoryRepository)):
    ls = InventoryService(repo).getAllInventoryTransaction()
    return ls

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=InventoryTransactionDTO)
def get_inventory_transaction(id: int, repo=Depends(InventoryRepository)):
    return InventoryService(repo).getInventoryTransaction(id)

@router.post("/", status_code=status.HTTP_200_OK, response_model=Message)
def create(request: InventoryTransaction, repo=Depends(InventoryRepository)):
    InventoryService(repo).createInventoryTransaction(request)
    return {"detail": "InventoryTransaction create successful."}

@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=Message)
def update(id: int, request: InventoryTransaction, repo=Depends(InventoryRepository)):
    InventoryService(repo).updateInventoryTransaction(id, request)
    return {"detail": "InventoryTransaction update successful."}

@router.delete("/{id}", status_code=status.HTTP_200_OK, response_model=Message)
def delete(id: int, repo=Depends(InventoryRepository)):
    InventoryService(repo).deleteInventoryTransaction(id)
    return {"detail": "InventoryTransaction delete successful."}

@router.post("/bulk", status_code=status.HTTP_200_OK, response_model=Message)
def bulk_delete(ids: BulkDelete, repo=Depends(InventoryRepository)):
    InventoryService(repo).deleteMulitpleInventoryTransaction(ids)
    return {"detail": "InventoryTransactions delete successful."}
