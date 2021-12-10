from db.base import User, Category
from sqlalchemy.orm import Session
from fastapi import HTTPException,status

def create(request, db: Session,current_user):
    user = db.query(User).filter(User.username == current_user.username).first()
    new_category = Category(name=request.name,description=request.description,created_user_id=user.id,updated_user_id=user.id)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

def readAll(db : Session):
    return db.query(Category).all()

def read(id : int, db : Session):
    category = db.query(Category).filter(Category.id==id).first()
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Category doesn't exist.")
    return category

def delete(id : int, db:Session):
    category = db.query(Category).filter(Category.id==id)
    if not category.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Cetegory doesn't exist.")
    category.delete(synchronize_session=False)
    db.commit()
    return

def update(id : int,request,db:Session,current_user):
    category = db.query(Category).filter(Category.id==id)
    if not category.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Cetegory doesn't exist.")
    user = db.query(User).filter(User.username == current_user.username).first()
    update_category = request.dict().copy()
    update_category.update({"updated_user_id": user.id})
    category.update(update_category)
    db.commit()
    return