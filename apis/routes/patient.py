from fastapi import APIRouter, Depends, status
from schemas.message import Message
from schemas.patient import Patient, showPatient
from core.services.patient import PatientService
from typing import List
from utils.oauth2 import extract_token_data
from schemas.token import TokenData
from infrastructure.repository.patient import PatientRepository

router = APIRouter(prefix="/patients", tags=["Patients"])

@router.get('/',status_code=status.HTTP_200_OK, response_model=List[showPatient])
def get_all_patients(repo=Depends(PatientRepository),tokenData: TokenData = Depends(extract_token_data)):
    return PatientService(repo,tokenData).getAllPatient()

@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=showPatient)
def get_patient(id: int, repo=Depends(PatientRepository),tokenData: TokenData = Depends(extract_token_data)):
    return PatientService(repo,tokenData).getPatient(id)

@router.post("/", status_code=status.HTTP_200_OK, response_model=Message)
def create(request: Patient, repo=Depends(PatientRepository),tokenData: TokenData = Depends(extract_token_data)):
    PatientService(repo,tokenData).addPatient(request)
    return {"detail": "Patient create successful."}

@router.put("/{id}",status_code=status.HTTP_200_OK,response_model=Message)
def update(id: int, request: Patient,repo=Depends(PatientRepository),tokenData: TokenData = Depends(extract_token_data)):
    PatientService(repo,tokenData).updatePatient(id,request)
    return {"detail": "Patient update successful."}

@router.delete("/{id}",status_code=status.HTTP_200_OK, response_model=Message)
def delete(id: int, repo=Depends(PatientRepository),tokenData: TokenData = Depends(extract_token_data)):
    PatientService(repo,tokenData).deletePatient(id)
    return {"detail": "Petient delete successful."}
