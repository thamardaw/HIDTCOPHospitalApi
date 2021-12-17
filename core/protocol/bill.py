from typing import Protocol

class BillProtocol(Protocol):
    def persist(self,data):
        ...
        
    def printBill(self,id:int):
        ...

    def getDraftedBill(self):
        ...

    def getPrintedBill(self):
        ...
        
    def getById(self,id:int):
        ...
    
    def updateBill(self,id:int,data):
        ...