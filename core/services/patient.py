from core.protocol.patient import PatientProtocol
from core.entity.patient import Patient
from typing import List

class PatientService:
    def __init__(self,patient_repo:PatientProtocol)->None:
        self.patient_repo = patient_repo
    
    def getAllPatient(self) -> List[Patient]:
        return self.patient_repo.list()
    
    def getPatient(self,id:int) -> Patient:
        return self.patient_repo.getById(id)
    
    def createPatient(self,patient:Patient) -> None:
        self.patient_repo.persist(patient)
        return 
    
    def updatePatient(self,id:int,patient:Patient) -> None:
        self.patient_repo.update(id,patient)
        return
    
    def deletePatient(self,id:int) -> None:
        self.patient_repo.delete(id)
        return 