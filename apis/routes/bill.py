from fastapi import APIRouter, Depends, status
from schemas.message import Message
from schemas.bill import Bill, showBill,showBillDailyClosing
from schemas.billItem import BillItem
from core.services.bill import BillService
from typing import List

router = APIRouter(prefix="/bill", tags=["Bills"])

@router.get('/drafted',status_code=status.HTTP_200_OK, response_model=List[showBill])
def get_all_drafted_bill(service=Depends(BillService)):
    return service.getAllDraftedBill()

@router.get('/printed',status_code=status.HTTP_200_OK, response_model=List[showBill])
def get_all_printed_bill(service=Depends(BillService)):
    return service.getAllPrintedBill()

@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=showBill)
def get_bill(id: int, service=Depends(BillService)):
    return service.getBill(id)

@router.get('/',status_code=status.HTTP_200_OK,response_model=List[showBillDailyClosing])
def get_bill_from_to(f: int,t:int, service=Depends(BillService)):
    return service.getAllFromAndTo(f,t)

@router.put('/print/{id}',status_code=status.HTTP_200_OK,response_model=Message)
def get_bill(id: int, service=Depends(BillService)):
    service.printBill(id)
    return {"detail": "Bill state update successful."}

@router.delete('/{billId}/billItem/{id}',status_code=status.HTTP_200_OK,response_model=Message)
def remove_bill_item(billId:int,id: int, service=Depends(BillService)):
    service.removeBillItem(billId,id)
    return {"detail": "Bill Item remove successful."}

@router.post("/{billId}/billItem/", status_code=status.HTTP_200_OK, response_model=Message)
def add_bill_item(billId:int,request: BillItem, service=Depends(BillService)):
    service.addBillItem(billId,request)
    return {"detail": "Bill Item add successful."}

@router.post("/", status_code=status.HTTP_200_OK, response_model=Message)
def create(request: Bill, service=Depends(BillService)):
    service.addBill(request)
    return {"detail": "Bill create successful."}

