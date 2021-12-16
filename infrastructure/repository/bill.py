from infrastructure.base_repo import BaseRepo
from utils.getCurrentUser import getCurrentUser
from infrastructure.models.bill import Bill
from core.entity.bill import Bill as BillDTO
from sqlalchemy.exc import SQLAlchemyError
from fastapi import status, HTTPException

SQLALCHEMY_ERROR = lambda exception,status_code = status.HTTP_500_INTERNAL_SERVER_ERROR: HTTPException(status_code=status_code,detail=str(exception))

class BillRepository(BaseRepo):
    def persist(self,bill):
        user = getCurrentUser(self._db,self._tokenData.username)
        new_bill = Bill(**bill,created_user_id=user.id,updated_user_id=user.id)
        new_bill = self.create(new_bill)
        return BillDTO.from_orm(new_bill)
        
    def getById(self,id: int):
        bill_orm = self.read(Bill,id)
        return BillDTO.from_orm(bill_orm)

    def getDraftedBill(self):
        try:
            bills = self._db.query(Bill).filter(Bill.printed_or_drafted=="drafted").all()
            return [BillDTO.from_orm(bill) for bill in bills]
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)
    
    def getPrintedBill(self):
        try:
            bills = self._db.query(Bill).filter(Bill.printed_or_drafted=="printed").all()
            return [BillDTO.from_orm(bill) for bill in bills]
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)

    def printBill(self,id: int):
        bill_orm = self.read(Bill,id)
        data = {"printed_or_drafted":"printed"}
        super().update(bill_orm,data)

    def updateBill(self,id: int,data):
        bill_orm = self.read(Bill,id)
        super().update(bill_orm,data)
        


