from typing import List
from infrastructure.base_repo import BaseRepo
from infrastructure.models.salesServiceItem import SalesServiceItem
from infrastructure.models.uom import Uom
from infrastructure.models.category import Category
from core.entity.salesServiceItem import SalesServiceItem as SalesServiceItemDTO, SalesServiceItemSmall as SalesServiceItemSmallDTO 
from core.entity.uom import Uom as UomDTO
from core.entity.category import Category as CategoryDTO

class SalesServiceItemRepository(BaseRepo):
    def persist(self,salesServiceItem) -> SalesServiceItemDTO:
        new_salesServiceItem = SalesServiceItem(**salesServiceItem.dict())
        new_salesServiceItem = self.create(new_salesServiceItem)
        return SalesServiceItemDTO.from_orm(new_salesServiceItem)

    def persistUom(self,uom) -> UomDTO:
        new_uom = Uom(**uom.dict())
        new_uom = self.create(new_uom)
        return UomDTO.from_orm(new_uom)

    def persistCategory(self,category) -> CategoryDTO:
        new_category = Category(**category.dict())
        new_category = self.create(new_category)
        return CategoryDTO.from_orm(new_category)
    
    def update(self,id,salesServiceItem):
        salesServiceItem_orm = self.read(SalesServiceItem,id)
        super().update(salesServiceItem_orm,salesServiceItem.dict())
        return

    def updateUom(self,id,uom):
        uom_orm = self.read(Uom,id)
        super().update(uom_orm,uom.dict())
        return

    def updateCategory(self,id,uom):
        uom_orm = self.read(Category,id)
        super().update(uom_orm,uom.dict())
        return

    def list(self) -> List[SalesServiceItemSmallDTO]:
        salesServiceItems = self.readAll(SalesServiceItem)
        return [SalesServiceItemSmallDTO.from_orm(salesServiceItem) for salesServiceItem in salesServiceItems]

    def listUom(self) -> List[UomDTO]:
        uoms = self.readAll(Uom)
        return [UomDTO.from_orm(uom) for uom in uoms]

    def listCategory(self) -> List[CategoryDTO]:
        categories = self.readAll(Category)
        return [CategoryDTO.from_orm(category) for category in categories]
    
    def delete(self,id):
        self.read(SalesServiceItem,id)
        super().delete(SalesServiceItem,id)
        return 

    def deleteUom(self,id):
        self.read(Uom,id)
        super().delete(Uom,id)
        return

    def deleteCategory(self,id):
        self.read(Category,id)
        super().delete(Category,id)
        
    def getById(self,id: int) -> SalesServiceItemDTO:
        salesServiceItem_orm = self.read(SalesServiceItem,id)
        return SalesServiceItemDTO.from_orm(salesServiceItem_orm)

    def getUomById(self,id: int) -> UomDTO:
        uom_orm = self.read(Uom,id)
        return UomDTO.from_orm(uom_orm)

    def getCategoryById(self,id: int) -> CategoryDTO:
        category_orm = self.read(Category,id)
        return CategoryDTO.from_orm(category_orm)
