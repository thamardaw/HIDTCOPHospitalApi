from infrastructure.base_repo import BaseRepo
from infrastructure.models.payment import Payment
from core.entity.payment import Payment as PaymentDTO
from fastapi import status, HTTPException
from utils.getCurrentUser import getCurrentUser

SQLALCHEMY_ERROR = lambda exception,status_code = status.HTTP_500_INTERNAL_SERVER_ERROR: HTTPException(status_code=status_code,detail=str(exception))

class PaymentRepository(BaseRepo):
    def persist(self,payment):
        user = getCurrentUser(self._db,self._tokenData.username)
        new_payment = Payment(**payment,created_user_id=user.id,updated_user_id=user.id)
        new_payment = self.create(new_payment)
        return 

    def list(self):
        payments = self.readAll(Payment)
        return [PaymentDTO.from_orm(payment) for payment in payments]


        


