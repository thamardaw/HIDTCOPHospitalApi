from core.protocol.dailyClosing import DailyClosingProtocol
from core.entity.dailyClosing import DailyClosing
from typing import List

class DailyClosingService:
    def __init__(self,dailyClosing_repo:DailyClosingProtocol)->None:
        self.dailyClosing_repo = dailyClosing_repo
    
    def getAllDailyClosing(self) -> List[DailyClosing]:
        return self.dailyClosing_repo.list()
    
    def getDailyClosing(self,id:int) -> DailyClosing:
        return self.dailyClosing_repo.getById(id)
    
    def closeCashierCounter(self,dailyClosing) -> None:
        new_dailyClosing = self.dailyClosing_repo.persist({"opening_balance":dailyClosing.opening_balance,"grand_total":dailyClosing.grand_total,"actual_amount":dailyClosing.actual_amount,"adjusted_amount":dailyClosing.adjusted_amount,"adjusted_reason":dailyClosing.adjusted_reason,"deposit_total":0,"bill_total":0})
        bill_total = 0
        deposit_total = 0
        for deposit in dailyClosing.closing_deposit_detail:
            deposit_total += deposit.amount
            self.dailyClosing_repo.persistClosingDepositDetail({"daily_closing_id":new_dailyClosing.id,"deposit_id":deposit.deposit_id,"amount":deposit.amount})
        for bill in dailyClosing.closing_bill_detail:
            bill_total += bill.amount
            self.dailyClosing_repo.persistClosingBillDetail({"daily_closing_id":new_dailyClosing.id,"bill_id":bill.bill_id,"amount":bill.amount})
        new_dailyClosing.deposit_total = deposit_total
        new_dailyClosing.bill_total = bill_total
        self.dailyClosing_repo.update(new_dailyClosing.id,new_dailyClosing)
        return 