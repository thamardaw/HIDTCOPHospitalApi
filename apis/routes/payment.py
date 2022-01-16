from fastapi import APIRouter, Depends, status
from schemas.message import Message
from core.services.bill import BillService
from infrastructure.repository.bill import BillRepository 

router = APIRouter(prefix="/payment", tags=["Payments"])

@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=Message)
def record_payment(id:int,repo=Depends(BillRepository)):
    BillService(repo).recordPayment(id)
    return {"detail": "Payment successful."}

    
