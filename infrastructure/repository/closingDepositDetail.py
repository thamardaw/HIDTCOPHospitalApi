from infrastructure.base_repo import BaseRepo
from infrastructure.models.closingDepositDetail import ClosingDepositDetail
from core.entity.closingDepositDetail import ClosingDepositDetail as ClosingDepositDetailDTO
from utils.getCurrentUser import getCurrentUser
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException, status

SQLALCHEMY_ERROR = lambda exception,status_code = status.HTTP_500_INTERNAL_SERVER_ERROR: HTTPException(status_code=status_code,detail=str(exception.__dict__['orig']))

class ClosingDepositDetailRepository(BaseRepo):
    def persist(self,closingDepositDetail):
        user = getCurrentUser(self._db,self._tokenData.username)
        new_closingDepositDetail = ClosingDepositDetail(**closingDepositDetail,created_user_id=user.id,updated_user_id=user.id)
        new_closingDepositDetail = self.create(new_closingDepositDetail)
        return ClosingDepositDetailDTO.from_orm(new_closingDepositDetail)
    
    def update(self,id,data):
        closingDepositDetail_orm = self.read(ClosingDepositDetail,id)
        super().update(closingDepositDetail_orm,data.dict())

    def list(self):
        closingDepositDetails = self.readAll(ClosingDepositDetail)
        return [ClosingDepositDetailDTO.from_orm(closingDepositDetail) for closingDepositDetail in closingDepositDetails]

    def listByDailyClosingId(self,id:int):
        try:
            closingDepositDetails = self._db.query(ClosingDepositDetail).filter(ClosingDepositDetail.daily_closing_id==id).all()
            return [ClosingDepositDetailDTO.from_orm(closingDepositDetail) for closingDepositDetail in closingDepositDetails]
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)
    
    def delete(self,closingDepositDetail):
        closingDepositDetail_orm = self.read(ClosingDepositDetail,closingDepositDetail.id)
        super().delete(closingDepositDetail_orm)
        
    def getById(self,id: int) :
        closingDepositDetail_orm = self.read(ClosingDepositDetail,id)
        return ClosingDepositDetailDTO.from_orm(closingDepositDetail_orm)
