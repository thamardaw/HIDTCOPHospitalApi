from infrastructure.base_repo import BaseRepo
from infrastructure.models.payment import Payment
from core.entity.payment import Payment as PaymentDTO
from fastapi import status, HTTPException
from utils.getCurrentUser import getCurrentUser
from sqlalchemy.exc import SQLAlchemyError

SQLALCHEMY_ERROR = lambda exception,status_code = status.HTTP_500_INTERNAL_SERVER_ERROR: HTTPException(status_code=status_code,detail=str(exception))
NOT_FOUND = HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Resource not found.')

class PaymentRepository(BaseRepo):
    def persist(self,payment):
        user = getCurrentUser(self._db,self._tokenData.username)
        new_payment = Payment(**payment,created_user_id=user.id,updated_user_id=user.id)
        new_payment = self.create(new_payment)
        return PaymentDTO.from_orm(new_payment)

    def list(self):
        payments = self.readAll(Payment)
        return [PaymentDTO.from_orm(payment) for payment in payments]

    def updatePayment(self,id: int):
        payment_orm = self.getByBillId(id)
        data = {"is_outstanding":False}
        super().update(payment_orm,data)

    def getByBillId(self,id:int):
        try:
            payment = self._db.query(Payment).filter(Payment.bill_id==id).first()
            if payment is None:
                raise NOT_FOUND
            return payment
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)

    def outstandingPayment(self):
        try:
            payments = self._db.query(Payment).filter(Payment.is_outstanding==True).all()
            return [PaymentDTO.from_orm(payment) for payment in payments]
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)

    def completedPayment(self):
        try:
            payments = self._db.query(Payment).filter(Payment.is_outstanding==False).all()
            return [PaymentDTO.from_orm(payment) for payment in payments]
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)