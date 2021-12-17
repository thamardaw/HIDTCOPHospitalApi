from core.protocol.billItem import BillItemProtocol
from core.entity.token import TokenData
from core.entity.billItem import BillItem
from typing import List

class BillItemService:
    def __init__(self,billItem_repo:BillItemProtocol,tokenData:TokenData)->None:
        self.billItem_repo = billItem_repo
        self.tokenData = tokenData
    
    def getAllBillItem(self) -> List[BillItem]:
        return self.billItem_repo.list()
    
    def getBillItem(self,id:int) -> BillItem:
        return self.billItem_repo.getById(id)
    
    def addBillItem(self,billItem:BillItem) -> BillItem:
        new_billItem = self.billItem_repo.persist(billItem)
        return new_billItem
    
    def updateBillItem(self,id:int,billItem:BillItem) -> BillItem:
        return self.billItem_repo.update(id,billItem)
    
    def deleteBillItem(self,id:int) -> None:
        billItem = self.billItem_repo.getById(id)
        self.billItem_repo.delete(billItem)

    def getAllByBillId(self,id:int) -> List[BillItem]:
        return self.billItem_repo.listByBillId(id)