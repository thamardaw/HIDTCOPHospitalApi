from db.models.patient import Patient
from sqlalchemy.orm import Session
from fastapi import HTTPException,status


def create(request, db: Session):
    new_patient = Patient(name=request.name,gender=request.gender,date_of_birth=request.date_of_birth,
                           age=request.age, address=request.address,
                           contact_details=request.contact_details, blood_group=request.blood_group
                           )
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return new_patient


def readAll( db: Session):
    return db.query(Patient).all()

def read(id, db:Session):
    patient = db.query(Patient).filter(Patient.patient_id==id).first()
    if not patient:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Patient doesn't exist.")
    return patient

def delete(id, db:Session):
    patient = db.query(Patient).filter(Patient.patient_id==id)
    if not patient.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Patient doesn't exist.")
    patient.delete(synchronize_session=False)
    db.commit()
    return

def update(id,request,db:Session):
    patient = db.query(Patient).filter(Patient.patient_id==id)
    if not patient.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Patient doesn't exist.")
    patient.update(request.dict())
    db.commit()
    return
