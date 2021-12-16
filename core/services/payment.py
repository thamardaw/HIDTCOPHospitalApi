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
    def make_payment(self,payment):
        patient = self.patient_repo.getById(payment.patient_id)
        bill = self.bill_repo.getById(payment.bill_id)
        self.payment_repo.persist({"patient_id":patient.id,"bill_id":bill.id,"total_amount":bill.total_amount,"total_deposit_amount":0,"collected_amount":bill.total_amount,"unpaid_amount":bill.total_amount})
        return 

    def getAllOutstandingBill(self):
        bills = self.bill_repo.getPrintedBill()
        payments = self.payment_repo.list()
        outstanding_bills = []
        if len(payments) != 0:
            if (len(payments) != len(bills)):
                for payment in payments:
                    for bill in bills:
                        if (bill.id != payment.bill_id and bill not in outstanding_bills):
                            outstanding_bills.append(bill)   
        else:
            outstanding_bills.extend(bills)
        return outstanding_bills
    
    def getAllCompletedBill(self):
        bills = self.bill_repo.getPrintedBill()
        payments = self.payment_repo.list()
        outstanding_bills = []
        if len(payments) != 0:
            for payment in payments:
                for bill in bills:
                    if (bill.id == payment.bill_id and bill not in outstanding_bills):
                        outstanding_bills.append(bill)
        return outstanding_bills