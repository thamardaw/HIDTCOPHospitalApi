from infrastructure.repository.deposit import DepositRepository
from core.entity.deposit import Deposit
from infrastructure.repository.patient import PatientRepository
from decorators.autoWired import autoWired
from typing import List

dependent_repos = {
    'deposit_repo' : DepositRepository,
    'patient_repo' : PatientRepository
}

@autoWired(dependencies=dependent_repos)
class DepositService:
    def getAllDeposit(self) -> List[Deposit]:
        return self.deposit_repo.list()
    
    def getDeposit(self,id:int) -> Deposit:
        return self.deposit_repo.getById(id)
    
    def addDeposit(self,deposit:Deposit) -> Deposit:
        patient = self.patient_repo.getById(deposit.patient_id)
        new_deposit = self.deposit_repo.persist({"patient_id":patient.id,"amount":deposit.amount,"remark":""})
        return new_deposit
    
    def updateDeposit(self,id:int,deposit:Deposit) -> Deposit:
        return self.deposit_repo.update(id,deposit)
    
    def deleteDeposit(self,id:int) -> None:
        deposit = self.deposit_repo.getById(id)
        self.deposit_repo.delete(deposit)