from typing import Protocol

class BillProtocol(Protocol):
    def persist(self,bill):
        ...

    def getById(self,id: int):
        ...

    def listCompletedBillFromAndTo(self,f:int,t:int):
        ...

    def listDraftBill(self):
        ...

    def listOutstandingBill(self):
        ...

    def listCompletedBill(self):
        ...

    def listCancelledBill(self):
        ...
    
    def listSmallCompletedBillFromAndTo(self,f:int,t:int):
        ...

    def listSmallDraftBill(self):
        ...

    def listSmallOutstandingBill(self):
        ...

    def listSmallCompletedBill(self):
        ...

    def listSmallCancelledBill(self):
        ...

    def update(self,id,bill):
        ...

    def persistBillItem(self,billItem):
        ...

    def deleteBillItem(self,id):
        ...

    def persistDeposit(self,deposit):
        ...

    def updateDeposit(self,id,deposit):
        ...

    def getDepositById(self,id: int):
        ...

    def updateBillItem(self,id:int,billItem):
        ...

    def getBillItemById(self,id: int):
        ...

    def listDepositFromAndTo(self,f:int,t:int):
        ...

    def listActiveDeposit(self):
        ...

    def listCancelledDeposit(self):
        ...

    def listActiveDepositByPatientId(self,id):
        ...

    def listUsedDeposit(self):
        ...
    
    def listSmallDepositFromAndTo(self,f:int,t:int):
        ...

    def listSmallActiveDeposit(self):
        ...

    def listSmallCancelledDeposit(self):
        ...

    def listSmallActiveDepositByPatientId(self,id):
        ...

    def listSmallUsedDeposit(self):
        ...

    def persistDepositUsed(self,depositUsed):
        ...

    def persistPayment(self,payment):
        ...

    def updatePayment(self,id,payment):
        ...