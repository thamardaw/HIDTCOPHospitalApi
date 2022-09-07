from typing import List
from fastapi import APIRouter, Depends, status
from schemas.message import Message
from schemas.bulkDelete import BulkDelete

from schemas.transactionType import TransactionType
from core.entity.transactionType import TransactionType as TransactionTypeDTO
# Call Service and Repo from Inventory
from core.services.inventory import InventoryService
from infrastructure.repository.inventory import InventoryRepository
from fastapi_pagination import Page,Params,paginate

router = APIRouter(prefix="/transaction_types", tags=["TransactionTypes"])

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[TransactionTypeDTO])
def get_all_transaction_types(repo=Depends(InventoryRepository)):
    ls = InventoryService(repo).getAllTransactionType()
    return ls

@router.get("/p", status_code=status.HTTP_200_OK, response_model=Page[TransactionTypeDTO])
def get_paginate_transaction_types(repo=Depends(InventoryRepository),params:Params=Depends()):
    return paginate(InventoryService(repo).getAllTransactionType(),params=params)
    

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=TransactionTypeDTO)
def get_transaction_type(id: int, repo=Depends(InventoryRepository)):
    return InventoryService(repo).getTransactionType(id)

@router.post("/", status_code=status.HTTP_200_OK, response_model=Message)
def create(request: TransactionType, repo=Depends(InventoryRepository)):
    InventoryService(repo).createTransactionType(request)
    return {"detail": "Transaction Type create successful."}

@router.put('/{id}', status_code=status.HTTP_200_OK, response_model=Message)
def update(id: int, request: TransactionType, repo=Depends(InventoryRepository)):
    InventoryService(repo).updateTransactionType(id, request)
    return {"detail": "Transaction Type update successful."}

@router.delete('/{id}', status_code=status.HTTP_200_OK, response_model=Message)
def delete(id: int, repo=Depends(InventoryRepository)):
    InventoryService(repo).deleteTransactionType(id)
    return {"detail": "Transaction Type delete successful."}

@router.post('/bulk', status_code=status.HTTP_200_OK, response_model=Message)
def bulk_delete(ids: BulkDelete, repo=Depends(InventoryRepository)):
    InventoryService(repo).deleteMulitpleTransactionType(ids)
    return {"detail": "Transaction Types delete successful."}

@router.post("/bulk_create",status_code=status.HTTP_200_OK, response_model=Message)
def bulk_create(request: List[TransactionType], repo=Depends(InventoryRepository)):
    InventoryService(repo).createMultipleTransactionType(request)
    return {"detail": "Transaction Types create successful."}