from fastapi import APIRouter, Depends, status
from schemas.message import Message
from schemas.deposit import Deposit
from core.entity.deposit import Deposit as DepositDTO
from infrastructure.repository.bill import BillRepository
from core.services.bill import BillService
from typing import List

router = APIRouter(prefix="/deposit", tags=["Deposit"])

@router.get('/active',status_code=status.HTTP_200_OK, response_model=List[DepositDTO])
def get_all_active_deposits(repo=Depends(BillRepository)):
    return BillService(repo).getAllActiveDeposit()

@router.get('/used',status_code=status.HTTP_200_OK, response_model=List[DepositDTO])
def get_all_used_deposits(repo=Depends(BillRepository)):
    return BillService(repo).getAllUsedDeposit()

@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=DepositDTO)
def get_deposit(id: int, repo=Depends(BillRepository)):
    return BillService(repo).getDeposit(id)

@router.get('/',status_code=status.HTTP_200_OK,response_model=List[DepositDTO])
def get_deposit_from_to(f: int,t:int, repo=Depends(BillRepository)):
    return BillService(repo).getAllDepositFromAndTo(f,t)

@router.post("/", status_code=status.HTTP_200_OK, response_model=Message)
def create(request: Deposit, repo=Depends(BillRepository)):
    BillService(repo).createDeposit(request)
    return {"detail": "Deposit create successful."}


