from infrastructure.base_repo import BaseRepo
from infrastructure.models.depositUsed import DepositUsed
from core.entity.depositUsed import DepositUsed as DepositUsedDTO
from utils.getCurrentUser import getCurrentUser

class DepositUsedRepository(BaseRepo):
    def persist(self,depositUsed):
        user = getCurrentUser(self._db,self._tokenData.username)
        new_depositUsed = DepositUsed(**depositUsed,created_user_id=user.id,updated_user_id=user.id)
        new_depositUsed = self.create(new_depositUsed)
        return DepositUsedDTO.from_orm(new_depositUsed)
    
    def update(self,id,data):
        depositUsed_orm = self.read(DepositUsed,id)
        super().update(depositUsed_orm,data.dict())

    def list(self):
        depositUseds = self.readAll(DepositUsed)
        return [DepositUsedDTO.from_orm(depositUsed) for depositUsed in depositUseds]
    
    def delete(self,depositUsed):
        depositUsed_orm = self.read(DepositUsed,depositUsed.id)
        super().delete(depositUsed_orm)
        
    def getById(self,id: int) :
        depositUsed_orm = self.read(DepositUsed,id)
        return DepositUsedDTO.from_orm(depositUsed_orm)