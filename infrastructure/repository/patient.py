from typing import List
from infrastructure.base_repo import BaseRepo
from infrastructure.models.patient import Patient
from core.entity.patient import Patient as PatientDTO

class PatientRepository(BaseRepo):
    def persist(self,patient) -> PatientDTO:
        new_patient = Patient(**patient.dict())
        new_patient = self.create(new_patient)
        return PatientDTO.from_orm(new_patient)
    
    def update(self,id,patient):
        patient_orm = self.read(Patient,id)
        super().update(patient_orm,patient.dict())
        return

    def list(self) -> List[PatientDTO]:
        patients = self.readAll(Patient)
        return [PatientDTO.from_orm(patient) for patient in patients]
    
    def delete(self,id):
        self.read(Patient,id)
        super().delete(Patient,id)
        return 
        
    def getById(self,id: int) -> PatientDTO:
        patient_orm = self.read(Patient,id)
        return PatientDTO.from_orm(patient_orm)
