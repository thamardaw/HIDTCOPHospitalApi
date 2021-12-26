from fastapi import APIRouter, Depends, status
from schemas.closingBillDetail import showClosingBillDetail
from schemas.closingDepositDetail import showClosingDepositDetail
from schemas.message import Message
from schemas.dailyClosing import DailyClosing, showDailyClosing
from core.services.dailyClosing import DailyClosingService
from typing import List

router = APIRouter(prefix="/dailyClosing", tags=["Daily Closing"])

@router.get('/',status_code=status.HTTP_200_OK, response_model=List[showDailyClosing])
def get_all_dailyClosings(service=Depends(DailyClosingService)):
    return service.getAllDailyClosing()

@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=showDailyClosing)
def get_dailyClosing(id: int, service=Depends(DailyClosingService)):
    return service.getDailyClosing(id)

@router.get('/{id}/deposits',status_code=status.HTTP_200_OK,response_model=List[showClosingDepositDetail])
def get_dailyClosing(id: int, service=Depends(DailyClosingService)):
    return service.getAllDeposit(id)

@router.get('/{id}/bills',status_code=status.HTTP_200_OK,response_model=List[showClosingBillDetail])
def get_dailyClosing(id: int, service=Depends(DailyClosingService)):
    return service.getAllBill(id)

@router.post("/", status_code=status.HTTP_200_OK, response_model=Message)
def create(request: DailyClosing, service=Depends(DailyClosingService)):
    service.addDailyClosing(request)
    return {"detail": "DailyClosing create successful."}
