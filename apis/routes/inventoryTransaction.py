from typing import List
from fastapi import APIRouter, Depends, status
from schemas.message import Message
from schemas.bulkDelete import BulkDelete

from schemas.inventoryTransaction import InventoryTransaction
from core.entity.inventoryTransaction import InventoryTransaction as InventoryTransactionDTO
# Call Service and Repo from Inventory
from core.services.inventory import InventoryService
from infrastructure.repository.inventory import InventoryRepository
from fastapi_pagination import Page,Params,paginate

router = APIRouter(prefix="/inventory_transactions", tags=["Inventory Transactions"])

@router.get('/', status_code=status.HTTP_200_OK, response_model=List[InventoryTransactionDTO])
def get_all_inventory_transactions(repo=Depends(InventoryRepository)):
    return InventoryService(repo).getAllInventoryTransaction()

@router.get('/p', status_code=status.HTTP_200_OK, response_model=Page[InventoryTransactionDTO])
def get_paginate_inventory_transactions(repo=Depends(InventoryRepository),params:Params=Depends()):
    return paginate(InventoryService(repo).getAllInventoryTransaction(),params=params)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=InventoryTransactionDTO)
def get_inventory_transaction(id: int, repo=Depends(InventoryRepository)):
    return InventoryService(repo).getInventoryTransaction(id)

@router.post("/", status_code=status.HTTP_200_OK, response_model=Message)
def create(request: InventoryTransaction, repo=Depends(InventoryRepository)):
    InventoryService(repo).createInventoryTransaction(request)
    return {"detail": "Inventory Transaction create successful."}

@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=Message)
def update(id: int, request: InventoryTransaction, repo=Depends(InventoryRepository)):
    InventoryService(repo).updateInventoryTransaction(id, request)
    return {"detail": "Inventory Transaction update successful."}

@router.delete("/{id}", status_code=status.HTTP_200_OK, response_model=Message)
def delete(id: int, repo=Depends(InventoryRepository)):
    InventoryService(repo).deleteInventoryTransaction(id)
    return {"detail": "Inventory Transaction delete successful."}

@router.post("/bulk", status_code=status.HTTP_200_OK, response_model=Message)
def bulk_delete(ids: BulkDelete, repo=Depends(InventoryRepository)):
    InventoryService(repo).deleteMulitpleInventoryTransaction(ids)
    return {"detail": "Inventory Transactions delete successful."}

@router.post("/bulk_create",status_code=status.HTTP_200_OK, response_model=Message)
def bulk_create(request: List[InventoryTransaction], repo=Depends(InventoryRepository)):
    InventoryService(repo).createMultipleInventoryTransaction(request)
    return {"detail": "Inventory Transactions create successful."}