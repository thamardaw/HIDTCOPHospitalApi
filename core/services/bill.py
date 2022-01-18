from core.entity.deposit import Deposit
from core.protocol.bill import BillProtocol
from core.entity.bill import Bill
from typing import List

class BillService:
    def __init__(self,bill_repo:BillProtocol)->None:
        self.bill_repo = bill_repo
    
    def getBill(self,id:int) -> Bill:
        return self.bill_repo.getById(id)

    def getAllDraftBill(self) -> List[Bill]:
        return self.bill_repo.listDraftBill()
    
    def getAllOutstandingBill(self) -> List[Bill]:
        return self.bill_repo.listOutstandingBill()

    def getAllCompletedBill(self) -> List[Bill]:
        return self.bill_repo.listCompletedBill()

    def getAllBillFromAndTo(self,f:int,t:int) -> List[Bill]:
        return self.bill_repo.listBillFromAndTo(f,t)

    def createBill(self,bill) -> None:
        new_bill = self.bill_repo.persist({"patient_id":bill.patient_id,"patient_name":bill.patient_name,"patient_phone":bill.patient_phone,"patient_address":bill.patient_address,"printed_or_drafted":"drafted","total_amount":0})
        total_amount = 0
        for billitem in bill.bill_items:
            billitem = billitem.dict()
            subtotal = billitem["quantity"] * billitem["price"]
            total_amount += subtotal
            b = dict(billitem,bill_id=new_bill.id,subtotal=subtotal)
            self.bill_repo.persistBillItem(b)
        self.bill_repo.update(new_bill.id,{"total_amount":total_amount})
        return
    
    def printBill(self,id:int) -> None:
        bill = self.bill_repo.getById(id)
        if bill.printed_or_drafted == "drafted":
            deposits = self.bill_repo.listActiveDepositByPatientId(bill.patient_id)
            total_deposit_amount = 0
            for deposit in deposits:
                total_deposit_amount += deposit.amount
            payment = self.bill_repo.persistPayment({"bill_id":bill.id,"total_amount":bill.total_amount,"total_deposit_amount":total_deposit_amount,"collected_amount":bill.total_amount-total_deposit_amount,"unpaid_amount":bill.total_amount-total_deposit_amount,"is_outstanding":True})
            bill_total = bill.total_amount
            for deposit in deposits:
                bill_total -= deposit.amount
                self.bill_repo.persistDepositUsed({"deposit_id":deposit.id,"payment_id":payment.id,"unpaid_amount":bill_total,"deposit_amount":deposit.amount})
            self.bill_repo.update(id,{"printed_or_drafted":"printed"})
        return

    def addBillItem(self,billId,billItem):
        bill_orm = self.bill_repo.getById(billId)
        subtotal_amount = billItem.price * billItem.quantity
        billItem = dict(billItem,bill_id=bill_orm.id,subtotal=subtotal_amount)
        self.bill_repo.persistBillItem(billItem)
        bill_orm = self.bill_repo.getById(billId)
        total_amount = 0
        for billItem in bill_orm.bill_items:
            total_amount += billItem.subtotal
        self.bill_repo.update(bill_orm.id,{"total_amount":total_amount})
        return

    def removeBillItem(self,billId:int,id:int):
        self.bill_repo.deleteBillItem(id)
        bill_orm = self.bill_repo.getById(billId)
        total_amount = 0
        for billItem in bill_orm.bill_items:
            total_amount += billItem.subtotal
        self.bill_repo.update(bill_orm.id,{"total_amount":total_amount})
        return

    def getAllActiveDeposit(self) -> List[Deposit]:
        return self.bill_repo.listActiveDeposit()

    def getAllUsedDeposit(self) -> List[Deposit]:
        return self.bill_repo.listUsedDeposit()

    def getAllDepositFromAndTo(self,f:int,t:int) -> List[Deposit]:
        return self.bill_repo.listDepositFromAndTo(f,t)

    def getDeposit(self,id:int) -> Deposit:
        return self.bill_repo.getDepositById(id)

    def createDeposit(self,deposit):
        self.bill_repo.persistDeposit(deposit)
        return

    def recordPayment(self,id):
        self.bill_repo.updatePayment(id,{"is_outstanding":False})
        return 