from typing import List
from infrastructure.base_repo import BaseRepo
from infrastructure.models.dailyClosing import DailyClosing
from infrastructure.models.closingBillDetail import ClosingBillDetail
from infrastructure.models.closingDepositDetail import ClosingDepositDetail
from core.entity.dailyClosing import DailyClosing as DailyClosingDTO, DailyClosingSmall as DailyClosingSmallDTO
from core.entity.closingBillDetail import ClosingBillDetail as ClosingBillDetailDTO
from core.entity.closingDepositDetail import ClosingDepositDetail as ClosingDepositDetailDTO 

class DailyClosingRepository(BaseRepo):
    def persist(self,dailyClosing) -> DailyClosingDTO:
        new_dailyClosing = DailyClosing(**dailyClosing)
        new_dailyClosing = self.create(new_dailyClosing)
        return DailyClosingDTO.from_orm(new_dailyClosing)

    def persistClosingBillDetail (self,closingBillDetail) -> ClosingBillDetailDTO:
        new_closingBillDetail = ClosingBillDetail(**closingBillDetail)
        new_closingBillDetail = self.create(new_closingBillDetail)
        return ClosingBillDetailDTO.from_orm(new_closingBillDetail)

    def persistClosingDepositDetail (self,closingDepositDetail) -> ClosingDepositDetailDTO:
        new_closingDepositDetail = ClosingDepositDetail(**closingDepositDetail)
        new_closingDepositDetail = self.create(new_closingDepositDetail)
        return ClosingDepositDetailDTO.from_orm(new_closingDepositDetail)

    def list(self) -> List[DailyClosingSmallDTO]:
        dailyClosings = self.readAll(DailyClosing)
        return [DailyClosingDTO.from_orm(dailyClosing) for dailyClosing in dailyClosings]
        
    def getById(self,id: int) -> DailyClosingDTO:
        dailyClosing_orm = self.read(DailyClosing,id)
        return DailyClosingDTO.from_orm(dailyClosing_orm)

    def update(self,id,dailyClosing):
        dailyClosing_orm = self.read(DailyClosing,id)
        super().update(dailyClosing_orm,dailyClosing.dict(exclude={'deposits','bills','created_user'}))
        return
