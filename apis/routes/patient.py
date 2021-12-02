from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from schemas.message import Message
from schemas.patient import Patient, showPatient
from db.repository import patient
from db.session import get_db
from typing import List
from services.oauth2 import get_current_user
from schemas.token import TokenData

router = APIRouter(prefix="/patients", tags=["Patients"])

@router.get('/',status_code=status.HTTP_200_OK, response_model=List[showPatient])
def get_all_patients(db: Session = Depends(get_db),current_user: TokenData = Depends(get_current_user)):
    return patient.readAll(db)


@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=showPatient)
def get_patient(id: int, db: Session = Depends(get_db),current_user: TokenData = Depends(get_current_user)):
    return patient.read(id,db)


@router.post("/", status_code=status.HTTP_200_OK, response_model=Message)
def create(request: Patient, db: Session = Depends(get_db),current_user: TokenData = Depends(get_current_user)):
    patient.create(request, db,current_user)
    return {"detail": "Patient create successful."}

@router.put("/{id}",status_code=status.HTTP_200_OK,response_model=Message)
def update(id: int, request: Patient,db: Session = Depends(get_db),current_user: TokenData = Depends(get_current_user)):
    patient.update(id,request,db,current_user)
    return {"detail": "Patient update successful."}


@router.delete("/{id}",status_code=status.HTTP_200_OK, response_model=Message)
def delete(id: int, db: Session = Depends(get_db),current_user: TokenData = Depends(get_current_user)):
    patient.delete(id,db)
    return {"detail": "Petient delete successful."}
