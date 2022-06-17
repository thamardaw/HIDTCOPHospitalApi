from typing import List
from fastapi import APIRouter, Depends, status
from schemas.message import Message
from schemas.billItem import BillItem
from core.entity.inventoryTransaction import InventoryTransaction
from core.services.inventory import InventoryService
from infrastructure.repository.inventory import InventoryRepository

router = APIRouter(prefix="/inventory", tags=["Inventory"])

@router.get('/dispense/{bill_id}', status_code=status.HTTP_200_OK, response_model=List[InventoryTransaction])
def get_all_dispensed_items_of_bill(bill_id: int, repo=Depends(InventoryRepository)):
    return InventoryService(repo).list_dispensed_items_of_bill(bill_id)

@router.post("/dispense", status_code=status.HTTP_200_OK, response_model=Message)
def dispense_items(request: List[BillItem], repo=Depends(InventoryRepository)):
    InventoryService(repo).dispense_items(request)
    return {"detail": "Items dispense successful."}

@router.post("/return", status_code=status.HTTP_200_OK, response_model=Message)
def return_item(request: BillItem, repo=Depends(InventoryRepository)):
    InventoryService(repo).return_items(request)
    return {"detail": "Items dispense successful."}
