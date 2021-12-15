from core.protocol.uom import UomProtocol
from core.entity.token import TokenData
from core.entity.uom import Uom
from typing import List

class UomService:
    def __init__(self,uom_repo:UomProtocol,tokenData:TokenData)->None:
        self.uom_repo = uom_repo
        self.tokenData = tokenData
    
    def getAllUom(self) -> List[Uom]:
        return self.uom_repo.list()
    
    def getUom(self,id:int) -> Uom:
        return self.uom_repo.getById(id)
    
    def addUom(self,uom:Uom) -> Uom:
        new_uom = self.uom_repo.persist(uom)
        return new_uom
    
    def updateUom(self,id:int,uom:Uom) -> Uom:
        return self.uom_repo.update(id,uom)
    
    def deleteUom(self,id:int) -> None:
        uom = self.uom_repo.getById(id)
        self.uom_repo.delete(uom)