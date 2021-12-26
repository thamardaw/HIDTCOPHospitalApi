from infrastructure.base_repo import BaseRepo
from infrastructure.models.dailyClosing import DailyClosing
from core.entity.dailyClosing import DailyClosing as DailyClosingDTO, DailyClosingFromPersist as DailyClosingFromPersistDTO
from utils.getCurrentUser import getCurrentUser

class DailyClosingRepository(BaseRepo):
    def persist(self,dailyClosing):
        user = getCurrentUser(self._db,self._tokenData.username)
        new_dailyClosing = DailyClosing(**dailyClosing,created_user_id=user.id,updated_user_id=user.id)
        new_dailyClosing = self.create(new_dailyClosing)
        return DailyClosingFromPersistDTO.from_orm(new_dailyClosing)
    
    def update(self,id,data):
        dailyClosing_orm = self.read(DailyClosing,id)
        super().update(dailyClosing_orm,data.dict())

    def list(self):
        dailyClosings = self.readAll(DailyClosing)
        return [DailyClosingDTO.from_orm(dailyClosing) for dailyClosing in dailyClosings]
    
    def delete(self,dailyClosing):
        dailyClosing_orm = self.read(DailyClosing,dailyClosing.id)
        super().delete(dailyClosing_orm)
        
    def getById(self,id: int) :
        dailyClosing_orm = self.read(DailyClosing,id)
        return DailyClosingDTO.from_orm(dailyClosing_orm)
