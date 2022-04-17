from typing import List
from infrastructure.base_repo import BaseRepo
from infrastructure.models.bill import Bill
from infrastructure.models.billItem import BillItem
from infrastructure.models.payment import Payment
from infrastructure.models.deposit import Deposit
from infrastructure.models.depositUsed import DepositUsed
from core.entity.bill import Bill as BillDTO
from core.entity.billItem import BillItem as BillItemDTO 
from core.entity.deposit import Deposit as DepositDTO
from core.entity.depositUsed import DepositUsed as DepositUsedDTO
from core.entity.payment import Payment as PaymentDTO
from sqlalchemy.exc import SQLAlchemyError
from exceptions.repo import SQLALCHEMY_ERROR

class BillRepository(BaseRepo):
    def persist(self,bill) -> BillDTO:
        new_bill = Bill(**bill)
        new_bill = self.create(new_bill)
        return BillDTO.from_orm(new_bill)

    def getById(self,id: int) -> BillDTO:
        bill_orm = self.read(Bill,id)
        return BillDTO.from_orm(bill_orm)

    def listBillFromAndTo(self,f:int,t:int) -> List[BillDTO]:
        try:
            bills = self._db.query(Bill).filter(Bill.is_cancelled==False, Bill.printed_or_drafted=="printed").filter(Bill.id>=f,Bill.id<=t).order_by(Bill.id.asc()).all()
            return [BillDTO.from_orm(bill) for bill in bills]
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)

    def listDraftBill(self) -> List[BillDTO]:
        try:
            bills = self._db.query(Bill).filter(Bill.is_cancelled==False,Bill.printed_or_drafted=="drafted").order_by(Bill.id.desc()).all()
            return [BillDTO.from_orm(bill) for bill in bills]
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)

    def listOutstandingBill(self) -> List[BillDTO]:
        try:
            bills = self._db.query(Bill,Payment).filter(Bill.is_cancelled==False,Bill.printed_or_drafted=="printed").filter(Payment.is_outstanding==True).filter(Bill.id == Payment.bill_id).order_by(Bill.id.desc()).all()
            return [BillDTO.from_orm(bill[0]) for bill in bills]
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)

    def listCompletedBill(self) -> List[BillDTO]:
        try:
            bills = self._db.query(Bill,Payment).filter(Bill.is_cancelled==False,Bill.printed_or_drafted=="printed").filter(Payment.is_outstanding==False).filter(Bill.id == Payment.bill_id).order_by(Bill.id.desc()).all()
            return [BillDTO.from_orm(bill[0]) for bill in bills]
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)

    def listCancelledBill(self) -> List[BillDTO]:
        try:
            bills = self._db.query(Bill).filter(Bill.is_cancelled==True).order_by(Bill.id.desc()).all()
            return [BillDTO.from_orm(bill) for bill in bills]
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)
    
    def update(self,id,bill):
        bill_orm = self.read(Bill,id)
        super().update(bill_orm,bill)
        return

    def persistBillItem(self,billItem) -> List[BillItemDTO]:
        new_billItem = BillItem(**billItem)
        new_billItem = self.create(new_billItem)
        return BillItemDTO.from_orm(new_billItem)

    def deleteBillItem(self,id):
        self.read(BillItem,id)
        super().delete(BillItem,id)
        return 

    def updateBillItem(self,id,billItem):
        billItem_orm = self.read(BillItem,id)
        super().update(billItem_orm,billItem)
        return 

    def getBillItemById(self,id: int) -> BillItemDTO:
        billItem_orm = self.read(BillItem,id)
        return BillItemDTO.from_orm(billItem_orm)
        
    def persistDeposit(self,deposit) -> DepositDTO:
        new_deposit = Deposit(**deposit.dict())
        new_deposit = self.create(new_deposit)
        return DepositDTO.from_orm(new_deposit)

    def updateDeposit(self,id,deposit):
        deposit_orm = self.read(Deposit,id)
        super().update(deposit_orm,deposit)
        return

    def getDepositById(self,id: int) -> DepositDTO:
        deposit_orm = self.read(Deposit,id)
        return DepositDTO.from_orm(deposit_orm)

    def listDepositFromAndTo(self,f:int,t:int) -> List[DepositDTO]:
        try:
            deposits = self._db.query(Deposit).filter(Deposit.is_cancelled==False).filter(Deposit.id>=f,Deposit.id<=t).all()
            return [DepositDTO.from_orm(deposit) for deposit in deposits]
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)

    def listActiveDeposit(self) -> List[DepositDTO]:
        try:
            used_deposits = self._db.query(Deposit,DepositUsed).filter(Deposit.id == DepositUsed.deposit_id).order_by(Deposit.id.desc()).all()
            deposits = self._db.query(Deposit).all()
            for used_deposit in used_deposits:
                deposits.remove(used_deposit[0])
            return [DepositDTO.from_orm(deposit) for deposit in deposits if deposit.is_cancelled == False]
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)

    def listCancelledDeposit(self) -> List[DepositDTO]:
        try:
            deposits = self._db.query(Deposit).filter(Deposit.is_cancelled==True).order_by(Deposit.id.desc()).all()
            return [DepositDTO.from_orm(deposit) for deposit in deposits]
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)

    def listActiveDepositByPatientId(self,id) -> List[DepositDTO]:
        try:
            used_deposits = self._db.query(Deposit,DepositUsed).filter(Deposit.patient_id==id).filter(Deposit.id == DepositUsed.deposit_id).all()
            deposits = self._db.query(Deposit).filter(Deposit.patient_id==id).all()
            for used_deposit in used_deposits:
                deposits.remove(used_deposit[0])
            return [DepositDTO.from_orm(deposit) for deposit in deposits if deposit.is_cancelled == False]
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)

    def listUsedDeposit(self) -> List[DepositDTO]:
        try:
            deposits = self._db.query(Deposit,DepositUsed).filter(Deposit.is_cancelled==False,Deposit.id == DepositUsed.deposit_id).order_by(Deposit.id.desc()).all()
            return [DepositDTO.from_orm(deposit[0]) for deposit in deposits ]
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)

    def persistDepositUsed(self,depositUsed) -> DepositUsedDTO:
        new_depositUsed = DepositUsed(**depositUsed)
        new_depositUsed = self.create(new_depositUsed)
        return DepositUsedDTO.from_orm(new_depositUsed)

    def persistPayment(self,payment) -> PaymentDTO:
        new_payment = Payment(**payment)
        new_payment = self.create(new_payment)
        return PaymentDTO.from_orm(new_payment)

    def updatePayment(self,id,payment):
        payment_orm = self.read(Payment,id)
        super().update(payment_orm,payment)
        return


