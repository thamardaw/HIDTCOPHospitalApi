from infrastructure.repository.dailyClosing import DailyClosingRepository
from infrastructure.repository.closingBillDetail import ClosingBillDetailRepository
from infrastructure.repository.closingDepositDetail import ClosingDepositDetailRepository
from core.entity.dailyClosing import DailyClosing
from decorators.autoWired import autoWired
from typing import List

dependent_repos = {
    'dailyClosing_repo' : DailyClosingRepository,
    'closingBill_repo' : ClosingBillDetailRepository,
    'closingDeposit_repo': ClosingDepositDetailRepository,
}

@autoWired(dependencies=dependent_repos)
class DailyClosingService:
    def getAllDailyClosing(self) -> List[DailyClosing]:
        return self.dailyClosing_repo.list()

    def getDailyClosing(self,id:int) -> DailyClosing:
        return self.dailyClosing_repo.getById(id)
    
    def addDailyClosing(self,dailyClosing:DailyClosing) -> DailyClosing:
        new_dailyClosing = self.dailyClosing_repo.persist({"opening_balance":dailyClosing.opening_balance,"grand_total":dailyClosing.grand_total,"actual_amount":dailyClosing.actual_amount,"adjusted_amount":dailyClosing.adjusted_amount,"adjusted_reason":dailyClosing.adjusted_reason,"deposit_total":0,"bill_total":0})
        bill_total = 0
        deposit_total = 0
        for deposit in dailyClosing.closing_deposit_detail:
            deposit_total += deposit.amount
            self.closingDeposit_repo.persist({"daily_closing_id":new_dailyClosing.id,"deposit_id":deposit.deposit_id,"amount":deposit.amount})
        for bill in dailyClosing.closing_bill_detail:
            bill_total += bill.amount
            self.closingBill_repo.persist({"daily_closing_id":new_dailyClosing.id,"bill_id":bill.bill_id,"amount":bill.amount})
        new_dailyClosing.deposit_total = deposit_total
        new_dailyClosing.bill_total = bill_total
        self.dailyClosing_repo.update(new_dailyClosing.id,new_dailyClosing)

    def getAllDeposit(self,id:int):
        return self.closingDeposit_repo.listByDailyClosingId(id)

    def getAllBill(self,id:int):
        return self.closingBill_repo.listByDailyClosingId(id)
