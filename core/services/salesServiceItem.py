from core.protocol.salesServiceItem import SalesServiceItemProtocol
from core.entity.salesServiceItem import SalesServiceItem,SalesServiceItemSmall
from core.entity.uom import Uom
from core.entity.category import Category
from exceptions.http import BAD_REQUEST
from typing import List
from fastapi.exceptions import HTTPException

class SalesServiceItemService:
    def __init__(self,salesServiceItem_repo:SalesServiceItemProtocol)->None:
        self.salesServiceItem_repo = salesServiceItem_repo
    
    def getAllSalesServiceItem(self) -> List[SalesServiceItemSmall]:
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
        # try :
        self.salesServiceItem_repo.persist(salesServiceItem)
        # except HTTPException as e:
        #     print(e.detail)
        return 

    def createMultipleSalesServiceItem(self,salesServiceItems) -> None:
        try:
            for salesServiceItem in salesServiceItems:
                self.salesServiceItem_repo.persist(salesServiceItem)
        except HTTPException as e:
            raise BAD_REQUEST(e.detail)
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
        try:
            self.salesServiceItem_repo.delete(id)
        except:
            raise BAD_REQUEST("Sales Service Item cannot be deleted.")
        return 

    def deleteMulitpleSalesServiceItem(self,ids) -> None:
        for id in ids.listOfId:
            try:
                self.salesServiceItem_repo.delete(id)
            except:
                raise BAD_REQUEST(f"Sales Service Item with id {id} cannot be deleted.")
        return

    def deleteUom(self,id:int) -> None:
        try:
            self.salesServiceItem_repo.deleteUom(id)
        except:
            raise BAD_REQUEST(f"UOM cannot be deleted.")
        return 

    def deleteMulitpleUom(self,ids) -> None:
        for id in ids.listOfId:
            try:
                self.salesServiceItem_repo.deleteUom(id)
            except:
                raise BAD_REQUEST(f"UOM with id {id} cannot be deleted.")
        return 

    def deleteCategory(self,id:int) -> None:
        try:
            self.salesServiceItem_repo.deleteCategory(id)
        except:
            raise BAD_REQUEST("Category cannot be deleted.")
        return 

    def deleteMulitpleCategory(self,ids) -> None:
        for id in ids.listOfId:
            try:
                self.salesServiceItem_repo.deleteCategory(id)
            except:
                raise BAD_REQUEST(f"Category with id {id} cannot be deleted.")
        return 