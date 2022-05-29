from typing import List
from fastapi import APIRouter, Depends, status
from schemas.message import Message
from schemas.bulkDelete import BulkDelete

from schemas.pharmacyItem import PharmacyItem
from core.entity.pharmacyItem import PharmacyItem as PharmacyItemDTO
# Call Service and Repo from Inventory
from core.services.inventory import InventoryService
from infrastructure.repository.inventory import InventoryRepository

router = APIRouter(prefix="/pharmacies", tags=["Pharmacies"])


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[PharmacyItemDTO])
def get_all_pharmacies(repo=Depends(InventoryRepository)):
    ls = InventoryService(repo).getAllPharmacyItem()
    return ls

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=PharmacyItemDTO)
def get_pharmacy(id: int, repo=Depends(InventoryRepository)):
    return InventoryService(repo).getPharmacyItem(id)

@router.post("/", status_code=status.HTTP_200_OK, response_model=Message)
def create(request: PharmacyItem, repo=Depends(InventoryRepository)):
    InventoryService(repo).createPharmacyItem(request)
    return {"detail": "Pharmacy create successful."}

@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=Message)
def update(id: int, request: PharmacyItem, repo=Depends(InventoryRepository)):
    InventoryService(repo).updatePharmacyItem(id, request)
    return {"detail": "Pharmacy update successful."}

@router.delete("/{id}", status_code=status.HTTP_200_OK, response_model=Message)
def delete(id: int, repo=Depends(InventoryRepository)):
    InventoryService(repo).deletePharmacyItem(id)
    return {"detail": "Pharmacy delete successful."}

@router.post("/bulk", status_code=status.HTTP_200_OK, response_model=Message)
def bulk_delete(ids: BulkDelete, repo=Depends(InventoryRepository)):
    InventoryService(repo).deleteMulitplePharmacyItem(ids)
    return {"detail": "Pharmacies delete successful."}