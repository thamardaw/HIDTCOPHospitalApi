from infrastructure.base_repo import BaseRepo
from infrastructure.models.closingBillDetail import ClosingBillDetail
from core.entity.closingBillDetail import ClosingBillDetail as ClosingBillDetailDTO
from utils.getCurrentUser import getCurrentUser
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException, status

SQLALCHEMY_ERROR = lambda exception,status_code = status.HTTP_500_INTERNAL_SERVER_ERROR: HTTPException(status_code=status_code,detail=str(exception.__dict__['orig']))

class ClosingBillDetailRepository(BaseRepo):
    def persist(self,closingBillDetail):
        user = getCurrentUser(self._db,self._tokenData.username)
        new_closingBillDetail = ClosingBillDetail(**closingBillDetail,created_user_id=user.id,updated_user_id=user.id)
        new_closingBillDetail = self.create(new_closingBillDetail)
        return ClosingBillDetailDTO.from_orm(new_closingBillDetail)
    
    def update(self,id,data):
        closingBillDetail_orm = self.read(ClosingBillDetail,id)
        super().update(closingBillDetail_orm,data.dict())

    def list(self):
        closingBillDetails = self.readAll(ClosingBillDetail)
        return [ClosingBillDetailDTO.from_orm(closingBillDetail) for closingBillDetail in closingBillDetails]

    def listByDailyClosingId(self,id:int):
        try:
            closingBillDetails = self._db.query(ClosingBillDetail).filter(ClosingBillDetail.daily_closing_id==id).all()
            return [ClosingBillDetailDTO.from_orm(closingBillDetail) for closingBillDetail in closingBillDetails]
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)
    
    def delete(self,closingBillDetail):
        closingBillDetail_orm = self.read(ClosingBillDetail,closingBillDetail.id)
        super().delete(closingBillDetail_orm)
        
    def getById(self,id: int) :
        closingBillDetail_orm = self.read(ClosingBillDetail,id)
        return ClosingBillDetailDTO.from_orm(closingBillDetail_orm)
