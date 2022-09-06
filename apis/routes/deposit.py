from fastapi import APIRouter, Depends, status
from schemas.message import Message
from schemas.deposit import Deposit
from core.entity.deposit import Deposit as DepositDTO
from core.entity.deposit import DepositSmall as DepositSmallDTO
from infrastructure.repository.bill import BillRepository
from core.services.bill import BillService
from typing import List
from fastapi_pagination import Page,Params,paginate

router = APIRouter(prefix="/deposit", tags=["Deposit"])

@router.get('/active',status_code=status.HTTP_200_OK, response_model=List[DepositSmallDTO])
def get_all_active_deposits(repo=Depends(BillRepository)):
    return BillService(repo).getAllActiveDeposit()

@router.get('/active/p',status_code=status.HTTP_200_OK, response_model=Page[DepositDTO])
def get_paginate_active_deposits(repo=Depends(BillRepository),params:Params=Depends()):
    return paginate(BillService(repo).getAllActiveDeposit(),params=params)

@router.get('/cancelled',status_code=status.HTTP_200_OK, response_model=List[DepositDTO])
def get_all_cancelled_deposits(repo=Depends(BillRepository)):
    return BillService(repo).getAllCancelledDeposit()

@router.get('/cancelled/p',status_code=status.HTTP_200_OK, response_model=Page[DepositDTO])
def get_paginate_cancelled_deposits(repo=Depends(BillRepository),params:Params=Depends()):
    return paginate(BillService(repo).getAllCancelledDeposit(),params=params)

@router.get('/active/{id}',status_code=status.HTTP_200_OK, response_model=List[DepositDTO])
def get_all_active_deposits_by_pateint_id(id: int,repo=Depends(BillRepository)):
    return BillService(repo).getAllActiveDepositByPatientId(id)

@router.get('/used',status_code=status.HTTP_200_OK, response_model=List[DepositSmallDTO])
def get_all_used_deposits(repo=Depends(BillRepository)):
    return BillService(repo).getAllUsedDeposit()

@router.get('/used/p',status_code=status.HTTP_200_OK, response_model=Page[DepositDTO])
def get_paginate_used_deposits(repo=Depends(BillRepository),params:Params=Depends()):
    return paginate(BillService(repo).getAllUsedDeposit(),params=params)

@router.get('/',status_code=status.HTTP_200_OK,response_model=List[DepositSmallDTO])
def get_deposit_from_to(f: int,t:int, repo=Depends(BillRepository)):
    return BillService(repo).getAllDepositFromAndTo(f,t)

@router.get('/p',status_code=status.HTTP_200_OK,response_model=Page[DepositDTO])
def get_paginate_deposit_from_to(f: int,t:int, repo=Depends(BillRepository),params:Params=Depends()):
    return paginate(BillService(repo).getAllDepositFromAndTo(f,t),params=params)

@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=DepositDTO)
def get_deposit(id: int, repo=Depends(BillRepository)):
    return BillService(repo).getDeposit(id)


@router.put('/cancel/{id}',status_code=status.HTTP_200_OK,response_model=Message)
def cancel_deposit(id: int, repo=Depends(BillRepository)):
    BillService(repo).cancelDeposit(id)
    return {"detail": "Deposit cancelled."}
    
@router.post("/", status_code=status.HTTP_200_OK, response_model=DepositDTO)
def create(request: Deposit, repo=Depends(BillRepository)):
    return BillService(repo).recordDepositReceive(request)
    # return {"detail": "Deposit create successful."}


