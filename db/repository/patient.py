from db.base import Patient, User
from sqlalchemy.orm import Session
from fastapi import HTTPException,status

def create(request, db: Session,current_user):
    user = db.query(User).filter(User.username == current_user.username).first()
    new_patient = Patient(name=request.name,gender=request.gender,date_of_birth=request.date_of_birth,
                           age=request.age, address=request.address,
                           contact_details=request.contact_details, 
                           created_user_id=user.id,updated_user_id=user.id
                           )
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return new_patient


def readAll(db : Session):
    return db.query(Patient).all()

def read(id : int, db : Session):
    patient = db.query(Patient).filter(Patient.id==id).first()
    if not patient:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Patient doesn't exist.")
    return patient

def delete(id : int, db:Session):
    patient = db.query(Patient).filter(Patient.id==id)
    if not patient.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Patient doesn't exist.")
    patient.delete(synchronize_session=False)
    db.commit()
    return

def update(id : int,request,db:Session,current_user):
    patient = db.query(Patient).filter(Patient.id==id)
    if not patient.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Patient doesn't exist.")
    user = db.query(User).filter(User.username == current_user.username).first()
    update_patient = request.dict().copy()
    update_patient.update({"updated_user_id": user.id})
    patient.update(update_patient)
    db.commit()
    return
