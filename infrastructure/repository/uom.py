from infrastructure.base import Uom, User
from sqlalchemy.orm import Session
from fastapi import HTTPException,status

def create(request, db: Session,current_user):
    user = db.query(User).filter(User.username == current_user.username).first()
    new_uom = Uom(name=request.name,description=request.description,created_user_id=user.id,updated_user_id=user.id)
    db.add(new_uom)
    db.commit()
    db.refresh(new_uom)
    return new_uom

def readAll(db : Session):
    return db.query(Uom).all()

def read(id : int, db : Session):
    uom = db.query(Uom).filter(Uom.id==id).first()
    if not uom:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="UOM doesn't exist.")
    return uom

def delete(id : int, db:Session):
    uom = db.query(Uom).filter(Uom.id==id)
    if not uom.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="UOM doesn't exist.")
    uom.delete(synchronize_session=False)
    db.commit()
    return

def update(id : int,request,db:Session,current_user):
    uom = db.query(Uom).filter(Uom.id==id)
    if not uom.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="UOM doesn't exist.")
    user = db.query(User).filter(User.username == current_user.username).first()
    update_uom = request.dict().copy()
    update_uom.update({"updated_user_id": user.id})
    uom.update(update_uom)
    db.commit()
    return