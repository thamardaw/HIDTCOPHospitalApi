from typing import Protocol

class DailyClosingProtocol(Protocol):
    def persist(self,dailyClosing):
        ...

    def persistClosingBillDetail (self,closingBillDetail):
        ...

    def persistClosingDepositDetail (self,closingDepositDetail):
        ...

    def list(self):
        ...

    def getById(self,id: int):
        ...

    def update(self,id,dailyClosing):
        ...