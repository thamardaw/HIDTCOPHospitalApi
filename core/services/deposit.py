from infrastructure.repository.deposit import DepositRepository
from core.entity.deposit import Deposit
from infrastructure.repository.patient import PatientRepository
from infrastructure.repository.depositUsed import DepositUsedRepository
from decorators.autoWired import autoWired
from typing import List

dependent_repos = {
    'deposit_repo' : DepositRepository,
    'patient_repo' : PatientRepository,
    'depositUsed_repo' : DepositUsedRepository
}

@autoWired(dependencies=dependent_repos)
class DepositService:
    def getAllDeposit(self) -> List[Deposit]:
        return self.deposit_repo.list()

    def getAllActiveDeposit(self):
        deposits = self.deposit_repo.list()
        depositUseds = self.depositUsed_repo.list()
        used_deposits = []
        if len(depositUseds) != 0:
            for depositUsed in depositUseds:
                for deposit in deposits:
                    if (deposit.id == depositUsed.deposit_id and deposit not in used_deposits):
                        used_deposits.append(deposit)
        for used_deposit in used_deposits:
            deposits.remove(used_deposit)
        return deposits

    def getAllFromAndTo(self,f:int,t:int):
        return self.deposit_repo.getFromAndTo(f,t)
    
    def getAllUsedDeposit(self):
        deposits = self.deposit_repo.list()
        depositUseds = self.depositUsed_repo.list()
        used_deposits = []
        if len(depositUseds) != 0:
            for depositUsed in depositUseds:
                for deposit in deposits:
                    if (deposit.id == depositUsed.deposit_id and deposit not in used_deposits):
                        used_deposits.append(deposit)
        return deposits

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