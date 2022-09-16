from core.protocol.patient import PatientProtocol
from core.entity.patient import Patient
from core.entity.patient import PatientSmall
from exceptions.http import BAD_REQUEST
from typing import List

class PatientService:
    def __init__(self,patient_repo:PatientProtocol)->None:
        self.patient_repo = patient_repo
    
    def getAllPatient(self) -> List[PatientSmall]:
        return self.patient_repo.listSmall()
    
    def getPatient(self,id:int) -> Patient:
        return self.patient_repo.getById(id)
    
    def createPatient(self,patient) -> None:
        self.patient_repo.persist(patient)
        return 
    
    def updatePatient(self,id:int,patient) -> None:
        self.patient_repo.update(id,patient)
        return
    
    def deletePatient(self,id:int) -> None:
        try:
            self.patient_repo.delete(id)
        except:
            raise BAD_REQUEST("Patient cannot be deleted.")
        return 

    # def deleteMulitplePatient(self,ids) -> Tuple[int,int]:
    #     count = 0
    #     for id in ids.listOfId:
    #         try:
    #             self.patient_repo.delete(id)
    #             count += 1
    #         except :
    #             pass
    #     return count, len(ids.listOfId)

    def deleteMulitplePatient(self,ids) -> None:
        for id in ids.listOfId:
            try:
                self.patient_repo.delete(id)
            except:
                raise BAD_REQUEST(f"Patient with id {id} cannot be deleted.")
        return 