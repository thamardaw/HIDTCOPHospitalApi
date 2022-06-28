from typing import Protocol, List
from core.entity.pharmacyItem import PharmacyItem as PharmacyItemDTO
from core.entity.inventoryItem import InventoryItem as InventoryItemDTO
from core.entity.inventoryTransaction import InventoryTransaction as InventoryTransactionDTO
from core.entity.transactionType import TransactionType as TransactionTypeDTO

# protocols of InventoryRepository
class InventoryProtocol(Protocol):
    def persistInventoryItem(self,inventoryItem) -> InventoryItemDTO:
        ...

    def persistPharmacyItem(self,pharmacyItem) -> PharmacyItemDTO:
        ...

    def persistInventoryTransaction(self,inventoryTransaction) -> InventoryTransactionDTO:
        ...

    def persistTransactionType(self,transactionType) -> TransactionTypeDTO:
        ...

    def updateInventoryItem(self,id,inventoryItem) -> None:
        ...

    def updatePharmacyItem(self,id,pharmacyItem) -> None:
        ...

    def updateInventoryTransaction(self,id,inventoryTransaction) -> None:
        ...

    def updateTransactionType(self,id,inventoryTransaction) -> None:
        ...

    def listInventoryItems(self) -> List[InventoryItemDTO]:
        ...

    def listPharmacyItems(self) -> List[PharmacyItemDTO]:
        ...

    def listInventoryTransactions(self) -> List[InventoryTransactionDTO]:
        ...

    def listInventoryTransactionsByNoteLikeAndType(self,note: str,type) -> List[InventoryTransactionDTO]:
        ...

    def listTransactionTypes(self) -> List[TransactionTypeDTO]:
        ...

    def deleteInventoryItem(self,id) -> None:
        ...

    def deletePharmacyItem(self,id) -> None:
        ...

    def deleteInventoryTransaction(self,id) -> None:
        ...

    def deleteTransactionType(self,id) -> None:
        ...

    def getInventoryItemById(self,id: int) -> InventoryItemDTO:
        ...

    def getInventoryItemBySalesServiceItemId(self,salesServiceItemId: int) -> InventoryItemDTO:
        ...

    def getPharmacyItemById(self,id: int) -> PharmacyItemDTO:
        ...

    def getInventoryTransactionById(self,id: int) -> InventoryTransactionDTO:
        ...

    def getInventoryTransactionByNoteAndType(self,note:str) -> InventoryTransactionDTO:
        ...

    def getTransactionTypeById(self,id: int) -> TransactionTypeDTO:
        ...
        

