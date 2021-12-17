from typing import Protocol

class UomProtocol(Protocol):
    def persist(self,data):
        ...
        
    def update(self,data):
        ...
        
    def delete(self,data):
        ...
        
    def list(self):
        ...
        
    def getById(self,id:int):
        ...