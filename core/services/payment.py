from infrastructure.repository.bill import BillRepository
from decorators.autoWired import autoWired
from infrastructure.repository.payment import PaymentRepository
from infrastructure.repository.patient import PatientRepository

dependent_repos = {
    'bill_repo': BillRepository,
    'payment_repo': PaymentRepository,
    'patient_repo': PatientRepository,
}

@autoWired(dependencies=dependent_repos)
class PaymentService:
    def record_payment(self,id):
        self.payment_repo.updatePayment(id)
        # bill = self.bill_repo.getById(payment.bill_id)
        # self.payment_repo.persist({"bill_id":bill.id,"total_amount":bill.total_amount,"total_deposit_amount":0,"collected_amount":bill.total_amount,"unpaid_amount":bill.total_amount})
        return 

    def getPaymentByBillId(self,id:int):
        return self.payment_repo.getByBillId(id)

    def getAllOutstandingBill(self):
        bills = self.bill_repo.getPrintedBill()
        payments = self.payment_repo.completedPayment()
        completed_bills = []
        if len(payments) != 0:
            for payment in payments:
                for bill in bills:
                    if (bill.id == payment.bill_id and bill not in completed_bills):
                        completed_bills.append(bill)
        for completed_bill in completed_bills:
            bills.remove(completed_bill)
        return bills
    
    def getAllCompletedBill(self):
        bills = self.bill_repo.getPrintedBill()
        payments = self.payment_repo.completedPayment()
        completed_bills = []
        if len(payments) != 0:
            for payment in payments:
                for bill in bills:
                    if (bill.id == payment.bill_id and bill not in completed_bills):
                        completed_bills.append(bill)
        return completed_bills
