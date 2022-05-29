from typing import List
from infrastructure.base_repo import BaseRepo
from infrastructure.models.inventoryItem import InventoryItem
from infrastructure.models.pharmacyItem import PharmacyItem
from infrastructure.models.inventoryTransaction import InventoryTransaction
from infrastructure.models.transactionType import TransactionType
from core.entity.inventoryItem import InventoryItem as InventoryItemDTO
from core.entity.pharmacyItem import PharmacyItem as PharmacyItemDTO
from core.entity.inventoryTransaction import InventoryTransaction as InventoryTransactionDTO
from core.entity.transactionType import TransactionType as TransactionTypeDTO

class InventoryRepository(BaseRepo):
    def persistInventoryItem(self,inventoryItem) -> InventoryItemDTO:
        new_inventoryItem = InventoryItem(**inventoryItem.dict())
        new_inventoryItem = self.create(new_inventoryItem)
        return InventoryItemDTO.from_orm(new_inventoryItem)

    def persistPharmacyItem(self,pharmacyItem) -> PharmacyItemDTO:
        new_pharmacyItem = PharmacyItem(**pharmacyItem.dict())
        new_pharmacyItem = self.create(new_pharmacyItem)
        return PharmacyItemDTO.from_orm(new_pharmacyItem)

    def persistInventoryTransaction(self,inventoryTransaction) -> InventoryTransactionDTO:
        new_inventoryTransaction = InventoryTransaction(**inventoryTransaction.dict())
        new_inventoryTransaction = self.create(new_inventoryTransaction)
        return InventoryTransactionDTO.from_orm(new_inventoryTransaction)

    def persistTransactionType(self,transactionType) -> TransactionTypeDTO:
        new_transactionType = TransactionType(**transactionType.dict())
        new_transactionType = self.create(new_transactionType)
        return TransactionTypeDTO.from_orm(new_transactionType)
    
    def updateInventoryItem(self,id,inventoryItem) -> None:
        inventoryItem_orm = self.read(InventoryItem,id)
        if type (inventoryItem) is dict:
            super().update(inventoryItem_orm,inventoryItem)
        else:
            super().update(inventoryItem_orm,inventoryItem.dict())
        return

    def updatePharmacyItem(self,id,pharmacyItem) -> None:
        pharmacyItem_orm = self.read(PharmacyItem,id)
        if type (pharmacyItem) is dict:
            super().update(pharmacyItem_orm,pharmacyItem)
        else:
            super().update(pharmacyItem_orm,pharmacyItem.dict())
        return

    def updateInventoryTransaction(self,id,inventoryTransaction) -> None:
        inventoryTransaction_orm = self.read(InventoryTransaction,id)
        if type (inventoryTransaction) is dict:
            super().update(inventoryTransaction_orm,inventoryTransaction)
        else:
            super().update(inventoryTransaction_orm,inventoryTransaction.dict())
        return

    def updateTransactionType(self,id,inventoryTransaction) -> None:
        inventoryTransaction_orm = self.read(TransactionType,id)
        if type (inventoryTransaction) is dict:
            super().update(inventoryTransaction_orm,inventoryTransaction)
        else:
            super().update(inventoryTransaction_orm,inventoryTransaction.dict())
        return

    def listInventoryItems(self) -> List[InventoryItemDTO]:
        inventoryItems = self.readAll(InventoryItem)
        return [InventoryItemDTO.from_orm(inventoryItem) for inventoryItem in inventoryItems]

    def listPharmacyItem(self) -> List[PharmacyItemDTO]:
        pharmacyItems = self.readAll(PharmacyItem)
        return [PharmacyItemDTO.from_orm(pharmacyItem) for pharmacyItem in pharmacyItems]

    def listInventoryTransaction(self) -> List[InventoryTransactionDTO]:
        inventoryTransactions = self.readAll(InventoryTransaction)
        return [InventoryTransactionDTO.from_orm(inventoryTransaction) for inventoryTransaction in inventoryTransactions]

    def listTransactionType(self) -> List[TransactionTypeDTO]:
        inventoryTransactions = self.readAll(TransactionType)
        return [TransactionTypeDTO.from_orm(inventoryTransaction) for inventoryTransaction in inventoryTransactions]

    def deleteInventoryItem(self,id) -> None:
        self.read(InventoryItem,id)
        super().delete(InventoryItem,id)
        return 

    def deletePharmacyItem(self,id) -> None:
        self.read(PharmacyItem,id)
        super().delete(PharmacyItem,id)
        return 

    def deleteInventoryTransaction(self,id) -> None:
        self.read(InventoryTransaction,id)
        super().delete(InventoryTransaction,id)
        return 

    def deleteTransactionType(self,id) -> None:
        self.read(TransactionType,id)
        super().delete(TransactionType,id)
        return 
        
    def getInventoryItemById(self,id: int) -> InventoryItemDTO:
        inventoryItem_orm = self.read(InventoryItem,id)
        return InventoryItemDTO.from_orm(inventoryItem_orm)

    def getPharmacyItemById(self,id: int) -> PharmacyItemDTO:
        inventoryItem_orm = self.read(PharmacyItem,id)
        return PharmacyItemDTO.from_orm(inventoryItem_orm)

    def getInventoryTransactionById(self,id: int) -> InventoryTransactionDTO:
        inventoryTransaction_orm = self.read(InventoryTransaction,id)
        return InventoryTransactionDTO.from_orm(inventoryTransaction_orm)

    def getTransactionTypeById(self,id: int) -> TransactionTypeDTO:
        inventoryTransaction_orm = self.read(TransactionType,id)
        return TransactionTypeDTO.from_orm(inventoryTransaction_orm)
