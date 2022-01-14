from infrastructure.base_repo import BaseRepo
from infrastructure.models.uom import Uom
from core.entity.uom import Uom as UomDTO

class UomRepository(BaseRepo):
    def persist(self,uom):
        new_uom = Uom(**uom.dict(),created_user_id=user.id,updated_user_id=user.id)
        new_uom = self.create(new_uom)
        return UomDTO.from_orm(new_uom)
    
    def update(self,id,data):
        uom_orm = self.read(Uom,id)
        super().update(uom_orm,data.dict())

    def list(self):
        uoms = self.readAll(Uom)
        return [UomDTO.from_orm(uom) for uom in uoms]
    
    def delete(self,uom):
        uom_orm = self.read(Uom,uom.id)
        super().delete(uom_orm)
        
    def getById(self,id: int) :
        uom_orm = self.read(Uom,id)
        return UomDTO.from_orm(uom_orm)
