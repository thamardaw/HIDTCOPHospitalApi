from core.protocol.inventory import InventoryProtocol
from core.entity.inventoryItem import InventoryItem
from core.entity.pharmacyItem import PharmacyItem
from core.entity.inventoryTransaction import InventoryTransaction
from core.entity.transactionType import TransactionType
from infrastructure.models.transactionType import type_enum
from exceptions.http import BAD_REQUEST
from typing import List

class InventoryService:
    def __init__(self,inventory_repo:InventoryProtocol)->None:
        self.inventory_repo = inventory_repo
    
    def getAllInventoryItem(self) -> List[InventoryItem]:
        return self.inventory_repo.listInventoryItems()

    def getAllInventoryTransaction(self) -> List[InventoryTransaction]:
        return self.inventory_repo.listInventoryTransactions()

    def getAllPharmacyItem(self) -> List[PharmacyItem]:
        return self.inventory_repo.listPharmacyItems()
    
    def getAllTransactionType(self) -> List[TransactionType]:
        return self.inventory_repo.listTransactionTypes()

    def getInventoryItem(self,id:int) -> InventoryItem:
        return self.inventory_repo.getInventoryItemById(id)

    def getInventoryTransaction(self,id:int) -> InventoryTransaction:
        return self.inventory_repo.getInventoryTransactionById(id)

    def getPharmacyItem(self,id:int) -> PharmacyItem:
        return self.inventory_repo.getPharmacyItemById(id)

    def getTransactionType(self,id:int) -> TransactionType:
        return self.inventory_repo.getTransactionTypeById(id)
    
    def createInventoryItem(self,inventoryItem) -> None:
        new_inventoryItem = self.inventory_repo.persistInventoryItem(inventoryItem)
        if inventoryItem.balance > 0:
            self.createInventoryTransaction\
                ({"inventory_item_id":new_inventoryItem.id,\
                "inventory_item_name":new_inventoryItem.name,\
                "transaction_type_name":"Adjustment In",\
                "transaction_type":type_enum.receive,\
                "quantity":new_inventoryItem.balance,\
                "opening_balance":0,\
                "closing_balance":new_inventoryItem.balance,\
                "unit":new_inventoryItem.unit,\
                "purchasing_price":new_inventoryItem.purchasing_price,\
                "selling_price":new_inventoryItem.sales_service_item.price})
        return 

    def createInventoryTransaction(self,inventoryTransaction) -> None:
        self.inventory_repo.persistInventoryTransaction(dict(inventoryTransaction))
        return 

    def createPharmacyItem(self,pharmacyItem) -> None:
        pharmacyItem = pharmacyItem.dict()
        inventoryItem = pharmacyItem["with_inventory"]
        pharmacyItem.pop("with_inventory")
        new_pharmacyItem = self.inventory_repo.persistPharmacyItem(pharmacyItem)
        if inventoryItem is None: return
        self.createInventoryItem(dict(inventoryItem,pharmacy_item_id=new_pharmacyItem.id))
        return 

    def createTransactionType(self,transactionType) -> None:
        self.inventory_repo.persistTransactionType(transactionType)
        return 
    
    def updateInventoryItem(self,id:int,inventoryItem) -> None:
        self.inventory_repo.updateInventoryItem(id,inventoryItem)
        return

    def updateInventoryTransaction(self,id:int,inventoryTransaction) -> None:
        self.inventory_repo.updateInventoryTransaction(id,inventoryTransaction)
        return

    def updatePharmacyItem(self,id:int,pharmacyItem) -> None:
        pharmacyItem = pharmacyItem.dict()
        pharmacyItem.pop("with_inventory")
        self.inventory_repo.updatePharmacyItem(id,pharmacyItem)
        return

    def updateTransactionType(self,id:int,transactionType) -> None:
        self.inventory_repo.updateTransactionType(id,transactionType)
        return
    
    def deleteInventoryItem(self,id:int) -> None:
        try:
            # self.inventory_repo.deleteInventoryItem(id)
            self.inventory_repo.updateInventoryItem(id,{"is_active":False})
        except:
            raise BAD_REQUEST("Inventory Item cannot be deleted.")
        return 

    def deleteInventoryTransaction(self,id:int) -> None:
        try:
            self.inventory_repo.deleteInventoryTransaction(id)
        except:
            raise BAD_REQUEST("Inventory Transaction cannot be deleted.")
        return 

    def deletePharmacyItem(self,id:int) -> None:
        try:
            self.inventory_repo.deletePharmacyItem(id)
        except:
            raise BAD_REQUEST("Pharmacy Item cannot be deleted.")
        return 

    def deleteTransactionType(self,id:int) -> None:
        try:
            self.inventory_repo.deleteTransactionType(id)
        except:
            raise BAD_REQUEST("Transaction Type cannot be deleted.")
        return 

    def deleteMulitpleInventoryItem(self,ids) -> None:
        for id in ids.listOfId:
            try:
                # self.inventory_repo.deleteInventoryItem(id)
                self.inventory_repo.updateInventoryItem(id,{"is_active":False})
            except:
                raise BAD_REQUEST(f"Inventory Item with id {id} cannot be deleted.")
        return 

    def deleteMulitpleInventoryTransaction(self,ids) -> None:
        for id in ids.listOfId:
            try:
                self.inventory_repo.deleteInventoryTransaction(id)
            except:
                raise BAD_REQUEST(f"Inventory Transaction with id {id} cannot be deleted.")
        return 

    def deleteMulitplePharmacyItem(self,ids) -> None:
        for id in ids.listOfId:
            try:
                self.inventory_repo.deletePharmacyItem(id)
            except:
                raise BAD_REQUEST(f"Pharmacy Item with id {id} cannot be deleted.")
        return 

    def deleteMulitpleTransactionType(self,ids) -> None:
        for id in ids.listOfId:
            try:
                self.inventory_repo.deleteTransactionType(id)
            except:
                raise BAD_REQUEST(f"Transaction Type with id {id} cannot be deleted.")
        return 