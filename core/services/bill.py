from infrastructure.repository.deposit import DepositRepository
from infrastructure.repository.depositUsed import DepositUsedRepository
from core.entity.bill import Bill 
from infrastructure.repository.billItem import BillItemRepository
from infrastructure.repository.patient import PatientRepository
from infrastructure.repository.bill import BillRepository
from infrastructure.repository.payment import PaymentRepository
from decorators.autoWired import autoWired
from typing import List

dependent_repos = {
    'bill_repo': BillRepository,
    'billItem_repo': BillItemRepository,
    'patient_repo' : PatientRepository,
    'payment_repo' : PaymentRepository,
    'deposit_repo' : DepositRepository,
    'depositUsed_repo' : DepositUsedRepository
}

@autoWired(dependencies=dependent_repos)
class BillService:
    def getAllDraftedBill(self) -> List[Bill]:
        drafted_bills = self.bill_repo.getDraftedBill()
        return drafted_bills

    def getAllPrintedBill(self) -> List[Bill]:
        printed_bills = self.bill_repo.getPrintedBill()
        return printed_bills

    def printBill(self,id:int):
        bill = self.bill_repo.getById(id)
        if bill.printed_or_drafted == "drafted":
            deposits = self.deposit_repo.getByPatientId(bill.patient_id)
            depositUseds = self.depositUsed_repo.list()
            used_deposits = []
            if len(depositUseds)!=0:
                for depositUsed in depositUseds:
                    for deposit in deposits:
                        if (deposit.id == depositUsed.deposit_id and deposit not in used_deposits):
                            used_deposits.append(deposit)
            for used_deposit in used_deposits:
                deposit.remove(used_deposit)
            total_deposit_amount = 0
            for deposit in deposits:
                total_deposit_amount += deposit.amount
            payment = self.payment_repo.persist({"bill_id":bill.id,"total_amount":bill.total_amount,"total_deposit_amount":total_deposit_amount,"collected_amount":bill.total_amount-total_deposit_amount,"unpaid_amount":bill.total_amount-total_deposit_amount,"is_outstanding":True})
            bill_total = bill.total_amount
            for deposit in deposits:
                bill_total -= deposit.amount
                self.depositUsed_repo.persist({"deposit_id":deposit.id,"payment_id":payment.id,"unpaid_amount":bill_total,"deposit_amount":deposit.amount})
            self.bill_repo.printBill(id)
    
    def getBill(self,id:int) -> Bill:
        return self.bill_repo.getById(id)
    
    def addBill(self,bill:Bill) -> Bill:
        patient = self.patient_repo.getById(bill.patient_id)
        new_bill = self.bill_repo.persist({"patient_id":patient.id,"patient_name":patient.name,"patient_phone":patient.contact_details,"patient_address":patient.address,"printed_or_drafted":"drafted","total_amount":0})
        total_amount = 0
        for billitem in bill.bill_items:
            billitem = billitem.dict()
            subtotal = billitem["quantity"] * billitem["price"]
            total_amount += subtotal
            b = dict(billitem,bill_id=new_bill.id,subtotal=subtotal)
            self.billItem_repo.persist(b)
        self.bill_repo.updateBill(new_bill.id,{"total_amount":total_amount})
        return

    def removeBillItem(self,billId:int,id:int):
        self.billItem_repo.delete(id)
        bill_orm = self.bill_repo.getById(billId)
        total_amount = 0
        for billItem in bill_orm.bill_items:
            total_amount += billItem.subtotal
        self.bill_repo.updateBill(billId,{"total_amount":total_amount})

    def addBillItem(self,billId,data):
        bill_orm = self.bill_repo.getById(billId)
        subtotal_amount = data.price * data.quantity
        billItem = dict(data,bill_id=bill_orm.id,subtotal=subtotal_amount)
        self.billItem_repo.persist(billItem)
        bill_orm = self.bill_repo.getById(billId)
        total_amount = 0
        for billItem in bill_orm.bill_items:
            total_amount += billItem.subtotal
        self.bill_repo.updateBill(billId,{"total_amount":total_amount})