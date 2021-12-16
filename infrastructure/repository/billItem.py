from infrastructure.base_repo import BaseRepo
from infrastructure.models.billItem import BillItem
from core.entity.billItem import BillItem as BillItemDTO
from utils.getCurrentUser import getCurrentUser
from fastapi import status, HTTPException
from sqlalchemy.exc import SQLAlchemyError

SQLALCHEMY_ERROR = lambda exception,status_code = status.HTTP_500_INTERNAL_SERVER_ERROR: HTTPException(status_code=status_code,detail=str(exception))

class BillItemRepository(BaseRepo):
    def persist(self,billItem):
        user = getCurrentUser(self._db,self._tokenData.username)
        new_billItem = BillItem(**billItem,created_user_id=user.id,updated_user_id=user.id)
        new_billItem = self.create(new_billItem)
        return BillItemDTO.from_orm(new_billItem)
    
    def update(self,id,data):
        billItem_orm = self.read(BillItem,id)
        super().update(billItem_orm,data.dict())

    def list(self):
        billItems = self.readAll(BillItem)
        return [BillItemDTO.from_orm(billItem) for billItem in billItems]
    
    def delete(self,id:int):
        billItem_orm = self.read(BillItem,id)
        super().delete(billItem_orm)
        
    def getById(self,id: int):
        billItem_orm = self.read(BillItem,id)
        return BillItemDTO.from_orm(billItem_orm)

    def listByBillId(self,id:int):
        try:
            billItems = self._db.query(BillItem).filter(BillItem.bill_id==id).all()
            return [BillItemDTO.from_orm(billItem) for billItem in billItems]
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)
