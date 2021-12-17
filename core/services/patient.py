from core.protocol.patient import PatientProtocol
from core.entity.token import TokenData
from core.entity.patient import Patient
from typing import List

class PatientService:
    def __init__(self,patient_repo:PatientProtocol,tokenData:TokenData)->None:
        self.patient_repo = patient_repo
        self.tokenData = tokenData
    
    def getAllPatient(self) -> List[Patient]:
        return self.patient_repo.list()
    
    def getPatient(self,id:int) -> Patient:
        return self.patient_repo.getById(id)
    
    def addPatient(self,patient:Patient) -> Patient:
        new_patient = self.patient_repo.persist(patient)
        return new_patient
    
    def updatePatient(self,id:int,patient:Patient) -> Patient:
        return self.patient_repo.update(id,patient)
    
    def deletePatient(self,id:int) -> None:
        patient = self.patient_repo.getById(id)
        self.patient_repo.delete(patient)