from fastapi import APIRouter, Depends, status
from schemas.message import Message
from schemas.deposit import Deposit, showDeposit
from core.services.deposit import DepositService
from typing import List

router = APIRouter(prefix="/deposit", tags=["Deposit"])

@router.get('/',status_code=status.HTTP_200_OK, response_model=List[showDeposit])
def get_all_deposits(service=Depends(DepositService)):
    return service.getAllDeposit()

@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=showDeposit)
def get_deposit(id: int, service=Depends(DepositService)):
    return service.getDeposit(id)

@router.post("/", status_code=status.HTTP_200_OK, response_model=Message)
def create(request: Deposit, service=Depends(DepositService)):
    service.addDeposit(request)
    return {"detail": "Deposit create successful."}

@router.put("/{id}",status_code=status.HTTP_200_OK,response_model=Message)
def update(id: int, request: Deposit,service=Depends(DepositService)):
    service.updateDeposit(id,request)
    return {"detail": "Deposit update successful."}

@router.delete("/{id}",status_code=status.HTTP_200_OK, response_model=Message)
def delete(id: int, service=Depends(DepositService)):
    service.deleteDeposit(id)
    return {"detail": "Deposit delete successful."}
