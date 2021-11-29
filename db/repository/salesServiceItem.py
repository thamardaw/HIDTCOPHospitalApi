from db.base import User, SalesServiceItem
from sqlalchemy.orm import Session
from fastapi import HTTPException,status

def create(request, db: Session,current_user):
    user = db.query(User).filter(User.username == current_user.username).first()
    new_salesServiceItem = SalesServiceItem(name=request.name,price=request.price,uom_id=request.uom_id,category_id=request.category_id,created_user_id=user.id,updated_user_id=user.id)
    db.add(new_salesServiceItem)
    db.commit()
    db.refresh(new_salesServiceItem)
    return new_salesServiceItem

def readAll(db : Session):
    return db.query(SalesServiceItem).all()

def read(id : int, db : Session):
    salesServiceItem = db.query(SalesServiceItem).filter(SalesServiceItem.id==id).first()
    if not salesServiceItem:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Sales Service Item doesn't exist.")
    return salesServiceItem

def delete(id : int, db:Session):
    salesServiceItem = db.query(SalesServiceItem).filter(SalesServiceItem.id==id)
    if not salesServiceItem.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Sales Service Item doesn't exist.")
    salesServiceItem.delete(synchronize_session=False)
    db.commit()
    return

def update(id : int,request,db:Session,current_user):
    salesServiceItem = db.query(SalesServiceItem).filter(SalesServiceItem.id==id)
    if not salesServiceItem.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Sales Service Item doesn't exist.")
    user = db.query(User).filter(User.username == current_user.username).first()
    update_salesServiceItem = request.dict().copy()
    update_salesServiceItem.update({"updated_user_id": user.id})
    salesServiceItem.update(update_salesServiceItem)
    db.commit()
    return