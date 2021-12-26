from infrastructure.base_repo import BaseRepo
from infrastructure.models.deposit import Deposit
from core.entity.deposit import Deposit as DepositDTO
from utils.getCurrentUser import getCurrentUser
from sqlalchemy.exc import SQLAlchemyError
from fastapi import status, HTTPException

SQLALCHEMY_ERROR = lambda exception,status_code = status.HTTP_500_INTERNAL_SERVER_ERROR: HTTPException(status_code=status_code,detail=str(exception))

class DepositRepository(BaseRepo):
    def persist(self,deposit):
        user = getCurrentUser(self._db,self._tokenData.username)
        new_deposit = Deposit(**deposit,created_user_id=user.id,updated_user_id=user.id)
        new_deposit = self.create(new_deposit)
        return DepositDTO.from_orm(new_deposit)
    
    def update(self,id,data):
        deposit_orm = self.read(Deposit,id)
        super().update(deposit_orm,data.dict())

    def list(self):
        deposits = self.readAll(Deposit)
        return [DepositDTO.from_orm(deposit) for deposit in deposits]

    def getFromAndTo(self,f : int,t: int):
        try:
            deposits = self._db.query(Deposit).filter(Deposit.id>=f).filter(Deposit.id<=t).all()
            return [DepositDTO.from_orm(deposit) for deposit in deposits]
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)
    
    def delete(self,deposit):
        deposit_orm = self.read(Deposit,deposit.id)
        super().delete(deposit_orm)
        
    def getById(self,id: int):
        deposit_orm = self.read(Deposit,id)
        return DepositDTO.from_orm(deposit_orm)

    def getByPatientId(self,id:int):
        try:
            deposits = self._db.query(Deposit).filter(Deposit.patient_id==id).all()
            return [DepositDTO.from_orm(deposit) for deposit in deposits]
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)