from fastapi import APIRouter, Depends, status
from infrastructure.repository.bill import BillRepository
from schemas.message import Message
from schemas.bill import Bill
from schemas.billItem import BillItem
from core.services.bill import BillService
from core.entity.bill import Bill as BillDTO
from typing import List
from datetime import date

router = APIRouter(prefix="/bill", tags=["Bill"])

@router.get('/drafted',status_code=status.HTTP_200_OK, response_model=List[BillDTO])
def get_all_drafted_bill(repo=Depends(BillRepository)):
    return BillService(repo).getAllDraftBill()

@router.get('/outstanding',status_code=status.HTTP_200_OK, response_model=List[BillDTO])
def get_all_outstanding_bill(repo=Depends(BillRepository)):
    return BillService(repo).getAllOutstandingBill()

@router.get('/completed',status_code=status.HTTP_200_OK, response_model=List[BillDTO])
def get_all_completed_bill(repo=Depends(BillRepository)):
    return BillService(repo).getAllCompletedBill()

@router.get('/cancelled',status_code=status.HTTP_200_OK, response_model=List[BillDTO])
def get_all_cancelled_bill(repo=Depends(BillRepository)):
    return BillService(repo).getAllCancelledBill()

@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=BillDTO)
def get_bill(id: int, repo=Depends(BillRepository)):
    return BillService(repo).getBill(id)

@router.get('/',status_code=status.HTTP_200_OK,response_model=List[BillDTO])
def get_completed_bill_from_to(f: date,t:date, repo=Depends(BillRepository)):
    return BillService(repo).getCompletedBillFromAndTo(f,t)

@router.put('/print/{id}',status_code=status.HTTP_200_OK,response_model=Message)
def to_printed(id: int, repo=Depends(BillRepository)):
    BillService(repo).printBill(id)
    return {"detail": "Bill state update successful."}

@router.put('/cancel/{id}',status_code=status.HTTP_200_OK,response_model=Message)
def cancel_bill(id: int, repo=Depends(BillRepository)):
    BillService(repo).cancelBill(id)
    return {"detail": "Bill cancelled."}

@router.delete('/{billId}/billItem/{id}',status_code=status.HTTP_200_OK,response_model=Message)
def remove_bill_item(billId:int,id: int, repo=Depends(BillRepository)):
    BillService(repo).removeBillItem(billId,id)
    return {"detail": "Bill Item remove successful."}

@router.put('/billItem/{id}',status_code=status.HTTP_200_OK,response_model=Message)
def update_bill_item(id: int,quantity: int, repo=Depends(BillRepository)):
    BillService(repo).updateBillItem(id,quantity)
    return {"detail": "Bill Item update successful."}

@router.post("/{billId}/billItem/", status_code=status.HTTP_200_OK, response_model=Message)
def add_bill_item(billId:int,request: BillItem, repo=Depends(BillRepository)):
    BillService(repo).addBillItem(billId,request)
    return {"detail": "Bill Item add successful."}

@router.post("/", status_code=status.HTTP_200_OK, response_model=BillDTO)
def create(request: Bill, repo=Depends(BillRepository)):
    return BillService(repo).createBill(request)
    # return {"detail": "Bill create successful."}

