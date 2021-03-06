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
from sqlalchemy.exc import SQLAlchemyError
from exceptions.repo import SQLALCHEMY_ERROR

class InventoryRepository(BaseRepo):
    def persistInventoryItem(self,inventoryItem) -> InventoryItemDTO:
        if type (inventoryItem) is dict:
            new_inventoryItem = InventoryItem(**inventoryItem)
        else:
            new_inventoryItem = InventoryItem(**inventoryItem.dict())
        new_inventoryItem = self.create(new_inventoryItem)
        return InventoryItemDTO.from_orm(new_inventoryItem)

    def persistPharmacyItem(self,pharmacyItem) -> PharmacyItemDTO:
        if type (pharmacyItem) is dict:
            new_pharmacyItem = PharmacyItem(**pharmacyItem)
        else:
            new_pharmacyItem = PharmacyItem(**pharmacyItem.dict())
        new_pharmacyItem = self.create(new_pharmacyItem)
        return PharmacyItemDTO.from_orm(new_pharmacyItem)

    def persistInventoryTransaction(self,inventoryTransaction) -> InventoryTransactionDTO:
        if type (inventoryTransaction) is dict:
            new_inventoryTransaction = InventoryTransaction(**inventoryTransaction)
        else:
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
        try:
            inventoryItems = self._db.query(InventoryItem).filter(InventoryItem.is_active==True).order_by(InventoryItem.id.desc()).all()
            return [InventoryItemDTO.from_orm(inventoryItem) for inventoryItem in inventoryItems]
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)

    def listPharmacyItems(self) -> List[PharmacyItemDTO]:
        pharmacyItems = self.readAll(PharmacyItem)
        return [PharmacyItemDTO.from_orm(pharmacyItem) for pharmacyItem in pharmacyItems]

    def listInventoryTransactions(self) -> List[InventoryTransactionDTO]:
        inventoryTransactions = self.readAll(InventoryTransaction)
        return [InventoryTransactionDTO.from_orm(inventoryTransaction) for inventoryTransaction in inventoryTransactions]

    def listInventoryTransactionsByNoteLikeAndType(self,note: str,type) -> List[InventoryTransactionDTO]:
        try:
            inventoryTransactions = self._db.query(InventoryTransaction).filter(InventoryTransaction.transaction_type==type).filter(InventoryTransaction.note.like(note)).all()
            return [InventoryTransactionDTO.from_orm(inventoryTransaction) for inventoryTransaction in inventoryTransactions]
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)

    def listTransactionTypes(self) -> List[TransactionTypeDTO]:
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
        try:
            inventoryItem_orm = self._db.query(InventoryItem).filter(InventoryItem.is_active==True).filter(InventoryItem.id==id).first()
            if inventoryItem_orm is not None: return InventoryItemDTO.from_orm(inventoryItem_orm)
            return None
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)

    def getInventoryItemBySalesServiceItemId(self,salesServiceItemId: int) -> InventoryItemDTO:
        try:
            inventoryItem_orm = self._db.query(InventoryItem).filter(InventoryItem.is_active==True).filter(InventoryItem.sales_service_item_id==salesServiceItemId).first()
            if inventoryItem_orm is not None: return InventoryItemDTO.from_orm(inventoryItem_orm)
            return None
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)
        
    def getPharmacyItemById(self,id: int) -> PharmacyItemDTO:
        inventoryItem_orm = self.read(PharmacyItem,id)
        return PharmacyItemDTO.from_orm(inventoryItem_orm)

    def getInventoryTransactionById(self,id: int) -> InventoryTransactionDTO:
        inventoryTransaction_orm = self.read(InventoryTransaction,id)
        return InventoryTransactionDTO.from_orm(inventoryTransaction_orm)

    def getInventoryTransactionByNoteAndType(self,note:str,type) -> InventoryTransactionDTO:
        try:
            inventoryTransaction_orm = self._db.query(InventoryTransaction).filter(InventoryTransaction.transaction_type==type).filter(InventoryTransaction.note==note).first()
            if inventoryTransaction_orm is not None: return InventoryTransactionDTO.from_orm(inventoryTransaction_orm)
            return None
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)

    def getTransactionTypeById(self,id: int) -> TransactionTypeDTO:
        inventoryTransaction_orm = self.read(TransactionType,id)
        return TransactionTypeDTO.from_orm(inventoryTransaction_orm)
