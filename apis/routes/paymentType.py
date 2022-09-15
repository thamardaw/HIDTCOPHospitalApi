from fastapi import APIRouter, Depends, status
from schemas.message import Message
from schemas.paymentType import PaymentType
from core.services.bill import BillService
from core.entity.paymentType import PaymentType as PaymentTypeDTO
from typing import List
from infrastructure.repository.bill import BillRepository
from fastapi_pagination import paginate,Page,Params

router = APIRouter(prefix="/payment_types", tags=["PaymentTypes"])

@router.get('/',status_code=status.HTTP_200_OK, response_model=List[PaymentTypeDTO])
def get_all_payment_types(repo=Depends(BillRepository)):
    ls  = BillService(repo).getAllPaymentType()
    return ls

@router.get('/p',status_code=status.HTTP_200_OK, response_model=Page[PaymentTypeDTO])
def get_paginate_payment_type(repo=Depends(BillRepository), params:Params= Depends()):
    ls  =BillService(repo).getAllPaymentType()
    return paginate(ls,params=params)

@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=PaymentTypeDTO)
def get_payment_type_by_id(id: int, repo=Depends(BillRepository)):
    return BillService(repo).getPaymentTypeById(id)

@router.post("/", status_code=status.HTTP_200_OK, response_model=Message)
def create(request: PaymentType, repo=Depends(BillRepository)):
    BillService(repo).createPaymentTYpe(request)
    return {"detail": "PaymentType create successful."}

@router.put("/{id}",status_code=status.HTTP_200_OK,response_model=Message)
def update(id: int, request: PaymentType,repo=Depends(BillRepository)):
    BillService(repo).updatePaymentType(id,request)
    return {"detail": "PaymentType update successful."}

@router.delete("/{id}",status_code=status.HTTP_200_OK, response_model=Message)
def delete(id: int, repo=Depends(BillRepository)):
    BillService(repo).deletePaymentType(id)
    return {"detail": "PaymentType delete successful."}

