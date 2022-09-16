from typing import Protocol

class PatientProtocol(Protocol):
    def persist(self,patient):
        ...
        
    def update(self,patient):
        ...
        
    def delete(self,id):
        ...
        
    def list(self):
        ...
    
    def listSmall(self):
        ...
        
    def getById(self,id):
        ...