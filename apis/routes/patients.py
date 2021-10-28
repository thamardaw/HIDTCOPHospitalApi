from os import name
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session, contains_alias
from schemas.message import Message
from schemas.patients import Patients
from db.session import get_db
from db.models import patient
from services.authentication import authenticate
from typing import List


router = APIRouter(prefix="/patients", tags=["Patients"])


@router.get('/', response_model=List[Patients])
def getallpatients(request: Patients, db: Session = Depends(get_db)):
    patients = db.query(Patients).all()
    # patients.read(request,db)
    return patients

# @router.post('/',response_model=Patients)
# def register_patients(request: PatientsEntry, db: Session = Depends(get_db)):
#     patients.register_patients(request,db)


@router.get('/{patientID}')
def get_patient(patientID: int):
    pass


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Message)
def create(request: Patients, db: Session = Depends(get_db)):
    new_patient = Patients(patient_id=request.patient_id,  name=request.name,
                           gender_enum=request.genderenum,
                           date_of_birth=request.date_of_birth,
                           age=request.age, address=request.address,
                           contact=request.contact_details, blood=request.blood_group
                           )
    db.add(new_patient)
    db.commit()
    #patients.create(request, db)
    return {"detail": "User create successful."}


@router.put("/{patientsID}")
def update_patients(patientsID: int):
    pass


@router.delete("/{patientID}")
def delete_user(patientID: int):
    pass
