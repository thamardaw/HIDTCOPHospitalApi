
from db.models.patient import Patient
from services.hashing import Hash
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from schemas import patients


def create(request: Patient, db: Session):

    new_patient = Patient(name=request.name, age=request.age, gender=request.genderenum, date_of_birth=request.date_of_birth,
                          address=request.address, contant=request.contact_details, bloodgroup=request.blood_group)
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return new_patient


async def read(request: Patient, db: Session):

    return


async def register_patients(user: patients.PatientsEntry, db: Session):
    patient_id = Patient.id
    name = Patient.name
    genderenum = Patient.genderenum

    date_of_birth = Patient.date_of_birth
    age = Patient.age
    address = Patient.address
    contact_details = Patient.contact_details
    blood_group = Patient.blood_group


async def delete_patients(user: patients.PatientsDelete, db: Session):
    db.delete(patients.PatientsDelete.patient_id)
