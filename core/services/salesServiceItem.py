from core.protocol.salesServiceItem import SalesServiceItemProtocol
from core.entity.salesServiceItem import SalesServiceItem
from core.entity.uom import Uom
from core.entity.category import Category
from typing import List

class SalesServiceItemService:
    def __init__(self,salesServiceItem_repo:SalesServiceItemProtocol)->None:
        self.salesServiceItem_repo = salesServiceItem_repo
    
    def getAllSalesServiceItem(self) -> List[SalesServiceItem]:
        return self.salesServiceItem_repo.list()

    def getAllUom(self) -> List[Uom]:
        return self.salesServiceItem_repo.listUom()

    def getAllCategory(self) -> List[Category]:
        return self.salesServiceItem_repo.listCategory()
    
    def getSalesServiceItem(self,id:int) -> SalesServiceItem:
        return self.salesServiceItem_repo.getById(id)

    def getUom(self,id:int) -> Uom:
        return self.salesServiceItem_repo.getUomById(id)

    def getCategory(self,id:int) -> Category:
        return self.salesServiceItem_repo.getCategoryById(id)
    
    def createSalesServiceItem(self,salesServiceItem) -> None:
        self.salesServiceItem_repo.persist(salesServiceItem)
        return 

    def createUom(self,uom) -> None:
        self.salesServiceItem_repo.persistUom(uom)
        return 

    def createCategory(self,category) -> None:
        self.salesServiceItem_repo.persistCategory(category)
        return 
    
    def updateSalesServiceItem(self,id:int,salesServiceItem) -> None:
        self.salesServiceItem_repo.update(id,salesServiceItem)
        return

    def updateUom(self,id:int,uom) -> None:
        self.salesServiceItem_repo.updateUom(id,uom)
        return

    def updateCategory(self,id:int,category) -> None:
        self.salesServiceItem_repo.updateCategory(id,category)
        return
    
    def deleteSalesServiceItem(self,id:int) -> None:
        self.salesServiceItem_repo.delete(id)
        return 

    def deleteUom(self,id:int) -> None:
        self.salesServiceItem_repo.deleteUom(id)
        return 

    def deleteCategory(self,id:int) -> None:
        self.salesServiceItem_repo.deleteCategory(id)
        return 