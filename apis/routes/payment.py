from fastapi import APIRouter, Depends, status
from schemas.message import Message
from schemas.bill import showBill
from schemas.payment import Payment
from typing import List
from core.services.payment import PaymentService

router = APIRouter(prefix="/payment", tags=["Payments"])

@router.get('/outstanding',status_code=status.HTTP_200_OK, response_model=List[showBill])
def get_all_outstanding_bill(service=Depends(PaymentService)):
    return service.getAllOutstandingBill()

@router.get('/completed',status_code=status.HTTP_200_OK,response_model=List[showBill])
def get_all_completed_bill(service=Depends(PaymentService)):
    return service.getAllCompletedBill()

@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=Message)
def make_payment(id:int, service=Depends(PaymentService)):
    service.make_payment(id)
    return {"detail": "Payment successful."}

