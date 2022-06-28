from typing import List
from fastapi import APIRouter, Depends, status
from schemas.message import Message
from schemas.bulkDelete import BulkDelete

from schemas.pharmacyItem import PharmacyItem
from core.entity.pharmacyItem import PharmacyItem as PharmacyItemDTO
# Call Service and Repo from Inventory
from core.services.inventory import InventoryService
from infrastructure.repository.inventory import InventoryRepository

router = APIRouter(prefix="/pharmacy_items", tags=["Pharmacy Items"])


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[PharmacyItemDTO])
def get_all_pharmacies(repo=Depends(InventoryRepository)):
    return InventoryService(repo).getAllPharmacyItem()

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=PharmacyItemDTO)
def get_pharmacy(id: int, repo=Depends(InventoryRepository)):
    return InventoryService(repo).getPharmacyItem(id)

@router.post("/", status_code=status.HTTP_200_OK, response_model=Message)
def create(request: PharmacyItem, repo=Depends(InventoryRepository)):
    InventoryService(repo).createPharmacyItem(request)
    return {"detail": "Pharmacy Item create successful."}

@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=Message)
def update(id: int, request: PharmacyItem, repo=Depends(InventoryRepository)):
    InventoryService(repo).updatePharmacyItem(id, request)
    return {"detail": "Pharmacy Item update successful."}

@router.delete("/{id}", status_code=status.HTTP_200_OK, response_model=Message)
def delete(id: int, repo=Depends(InventoryRepository)):
    InventoryService(repo).deletePharmacyItem(id)
    return {"detail": "Pharmacy Item delete successful."}

@router.post("/bulk", status_code=status.HTTP_200_OK, response_model=Message)
def bulk_delete(ids: BulkDelete, repo=Depends(InventoryRepository)):
    InventoryService(repo).deleteMulitplePharmacyItem(ids)
    return {"detail": "Pharmacy Items delete successful."}

@router.post("/bulk_create", status_code=status.HTTP_200_OK, response_model=Message)
def bulk_create(request: List[PharmacyItem], repo=Depends(InventoryRepository)):
    InventoryService(repo).createMultiplePharmacyItem(request)
    return {"detail": "Pharmacy Items create successful."}