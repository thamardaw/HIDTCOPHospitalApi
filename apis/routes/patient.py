from fastapi import APIRouter, Depends, status
from schemas.message import Message
from schemas.patient import Patient
from schemas.bulkDelete import BulkDelete
from core.services.patient import PatientService
from core.entity.patient import Patient as PatientDTO
from core.entity.patient import PatientSmall as PatientSmallDTO
from typing import List
from infrastructure.repository.patient import PatientRepository
from fastapi_pagination import paginate,Page,Params

router = APIRouter(prefix="/patients", tags=["Patients"])

@router.get('/',status_code=status.HTTP_200_OK, response_model=List[PatientSmallDTO])
def get_all_patients(repo=Depends(PatientRepository)):
    ls  = PatientService(repo).getAllPatient()
    return ls

@router.get('/p',status_code=status.HTTP_200_OK, response_model=Page[PatientDTO])
def get_paginate_patients(repo=Depends(PatientRepository), params:Params= Depends()):
    ls  = PatientService(repo).getAllPatient()
    return paginate(ls,params=params)

@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=PatientDTO)
def get_patient(id: int, repo=Depends(PatientRepository)):
    return PatientService(repo).getPatient(id)

@router.post("/", status_code=status.HTTP_200_OK, response_model=Message)
def create(request: Patient, repo=Depends(PatientRepository)):
    PatientService(repo).createPatient(request)
    return {"detail": "Patient create successful."}

@router.put("/{id}",status_code=status.HTTP_200_OK,response_model=Message)
def update(id: int, request: Patient,repo=Depends(PatientRepository)):
    PatientService(repo).updatePatient(id,request)
    return {"detail": "Patient update successful."}

@router.delete("/{id}",status_code=status.HTTP_200_OK, response_model=Message)
def delete(id: int, repo=Depends(PatientRepository)):
    PatientService(repo).deletePatient(id)
    return {"detail": "Patient delete successful."}

@router.post("/bulk",status_code=status.HTTP_200_OK, response_model=Message)
def bulk_delete(ids: BulkDelete, repo=Depends(PatientRepository)):
    PatientService(repo).deleteMulitplePatient(ids)
    return {"detail": "Patients delete successful."}

