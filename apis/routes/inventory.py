from typing import List
from fastapi import APIRouter, Depends, status
from core.entity.inventoryItem import InventoryItem
from schemas.message import Message
from schemas.billItem import InvBillItem
from core.entity.inventoryTransaction import InventoryTransaction
from core.services.inventory import InventoryService
from infrastructure.repository.inventory import InventoryRepository

router = APIRouter(prefix="/inventory", tags=["Inventory"])

@router.get('/dispense/{bill_id}', status_code=status.HTTP_200_OK, response_model=List[InventoryTransaction])
def get_all_dispensed_items_of_bill(bill_id: int, repo=Depends(InventoryRepository)):
    return InventoryService(repo).list_dispensed_items_of_bill(bill_id)

@router.post('/', status_code=status.HTTP_200_OK, response_model=List[InventoryItem])
def get_all_inventory_item_by_bill_items(request: List[InvBillItem], repo=Depends(InventoryRepository)):
    return InventoryService(repo).list_inventory_item_by_bill_items(request)

@router.post("/dispense", status_code=status.HTTP_200_OK, response_model=Message)
def dispense_items(request: List[InvBillItem], repo=Depends(InventoryRepository)):
    print(request)
    InventoryService(repo).dispense_items(request)
    return {"detail": "Items dispense successful."}

@router.post("/return", status_code=status.HTTP_200_OK, response_model=Message)
def return_item(request: InvBillItem, repo=Depends(InventoryRepository)):
    InventoryService(repo).return_item(request)
    return {"detail": "Item return successful."}

@router.post("/returns", status_code=status.HTTP_200_OK, response_model=Message)
def return_item(request: List[InvBillItem], repo=Depends(InventoryRepository)):
    InventoryService(repo).return_items(request)
    return {"detail": "Item return successful."}
