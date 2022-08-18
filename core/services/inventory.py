from fastapi import HTTPException
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
        if type(inventoryItem) is not dict:
            inventoryItem = inventoryItem.dict()
        if self.inventory_repo.getInventoryItemBySalesServiceItemId(inventoryItem["sales_service_item_id"]): 
            raise BAD_REQUEST(f'Sales Item ID {inventoryItem["sales_service_item_id"]} already in use.')
        initial_balance = inventoryItem["balance"]
        inventoryItem["balance"] = 0
        new_inventoryItem = self.inventory_repo.persistInventoryItem(inventoryItem)
        if initial_balance > 0:
            self.createInventoryTransaction\
                ({"inventory_item_id":new_inventoryItem.id,\
                "inventory_item_name":new_inventoryItem.name,\
                "transaction_type_name":"Adjustment In",\
                "transaction_type":type_enum.receive,\
                "quantity":initial_balance,\
                "unit":new_inventoryItem.unit,\
                "purchasing_price":new_inventoryItem.purchasing_price,\
                "selling_price": new_inventoryItem.sales_service_item.price if new_inventoryItem.sales_service_item else  0})
        return 
    
    def createMultipleInventoryItem(self,inventoryItems) -> None:
        try:
            for inventoryItem in inventoryItems:
                self.createInventoryItem(inventoryItem)
        except HTTPException as e:
            raise BAD_REQUEST(e.detail)
        return


    def dispense_item(self,billItem) -> None:
        note = f"{billItem.bill_id}, {billItem.id}"
        if self.inventory_repo.getInventoryTransactionByNoteAndType(note, type_enum.issue) is not None: return 
        inventoryItem = self.inventory_repo.getInventoryItemBySalesServiceItemId(billItem.sales_service_item_id)
        if inventoryItem is None: return
        self.createInventoryTransaction\
            ({"inventory_item_id":inventoryItem.id,\
            "inventory_item_name":inventoryItem.name,\
            "transaction_type_name":"Adjustment Out",\
            "transaction_type":type_enum.issue,\
            "quantity":billItem.quantity,\
            "unit":inventoryItem.unit,\
            "purchasing_price":inventoryItem.purchasing_price,\
            "selling_price":inventoryItem.sales_service_item.price,\
            "note":note})
        return 

    def dispense_items(self, billItems) -> None:
        for billItem in billItems:
            self.dispense_item(billItem)
        return

    def list_dispensed_items_of_bill(self,bill_id) -> List[InventoryTransaction]:
        iss_invtxs = self.inventory_repo.listInventoryTransactionsByNoteLikeAndType(f"{bill_id},%",type_enum.issue)
        iss_invtxs_copy = iss_invtxs.copy()
        rec_invtxs = self.inventory_repo.listInventoryTransactionsByNoteLikeAndType(f"{bill_id},%",type_enum.receive)
        for iss_invtx in iss_invtxs:
            for rec_invtx in rec_invtxs:
                if iss_invtx.note == rec_invtx.note:
                    iss_invtxs_copy.remove(iss_invtx)
        return iss_invtxs_copy

    def list_inventory_item_by_bill_items(self,billItems) -> List[InventoryItem]:
        inventoryItem_list = []
        for billItem in billItems:
            inventoryItem = self.inventory_repo.getInventoryItemBySalesServiceItemId(billItem.sales_service_item_id)
            if inventoryItem is not None: inventoryItem_list.append(inventoryItem)
        return inventoryItem_list

    def return_item(self, billItem) -> None:
        note = f"{billItem.bill_id}, {billItem.id}"
        inventoryTransaction = self.inventory_repo.getInventoryTransactionByNoteAndType(note,type_enum.issue)
        if inventoryTransaction is None: return
        inventoryItem = self.inventory_repo.getInventoryItemById(inventoryTransaction.inventory_item_id)
        if inventoryItem is None: return
        self.createInventoryTransaction\
            ({"inventory_item_id":inventoryItem.id,\
            "inventory_item_name":inventoryItem.name,\
            "transaction_type_name":"Adjustment In",\
            "transaction_type":type_enum.receive,\
            "quantity":billItem.quantity,\
            "unit":inventoryItem.unit,\
            "purchasing_price":inventoryItem.purchasing_price,\
            "selling_price":inventoryItem.sales_service_item.price,\
            "note":note})
        # self.inventory_repo.deleteInventoryTransaction(inventoryTransaction.id)
        return

    def return_items(self, billItems) -> None:
        for billItem in billItems:
            self.return_item(billItem)
        return 

    def createInventoryTransaction(self,inventoryTransaction) -> None:
        if type(inventoryTransaction) is not dict:
            inventoryTransaction = inventoryTransaction.dict()
        inventoryItem = self.inventory_repo.getInventoryItemById(inventoryTransaction["inventory_item_id"])
        total = inventoryItem.balance
        if inventoryTransaction["transaction_type"] == type_enum.receive:
            total = inventoryItem.balance + inventoryTransaction["quantity"]
            self.inventory_repo.updateInventoryItem\
                (inventoryItem.id,{"balance":total})
        elif inventoryTransaction["transaction_type"] == type_enum.issue:
            if inventoryTransaction["quantity"] > inventoryItem.balance:
                raise BAD_REQUEST("Not enough "+ inventoryTransaction["inventory_item_name"] +" in inventory.")
            total = inventoryItem.balance - inventoryTransaction["quantity"]
            self.inventory_repo.updateInventoryItem\
                (inventoryItem.id,{"balance":total})
        self.inventory_repo.persistInventoryTransaction(dict(inventoryTransaction,opening_balance=inventoryItem.balance,closing_balance=total))
        return 

    def createMultipleInventoryTransaction(self,inventoryTransactions) -> None:
        try:
            for inventoryTransaction in inventoryTransactions:
                self.createInventoryTransaction(inventoryTransaction)
        except HTTPException as e:
            raise BAD_REQUEST(e.detail)
        return

    def createPharmacyItem(self,pharmacyItem) -> None:
        pharmacyItem = pharmacyItem.dict()
        inventoryItem = pharmacyItem["with_inventory"]
        pharmacyItem.pop("with_inventory")
        new_pharmacyItem = self.inventory_repo.persistPharmacyItem(pharmacyItem)
        if inventoryItem is None: return
        self.createInventoryItem(dict(inventoryItem,pharmacy_item_id=new_pharmacyItem.id))
        return 

    def createMultiplePharmacyItem(self,pharmacyItems) -> None:
        try:
            for pharmacyItem in pharmacyItems:
                self.createPharmacyItem(pharmacyItem)
        except HTTPException as e:
            raise BAD_REQUEST(e.detail)
        return

    def createTransactionType(self,transactionType) -> None:
        self.inventory_repo.persistTransactionType(transactionType)
        return 
    
    def createMultipleTransactionType(self,transactionTypes) -> None:
        try:
            for transactionType in transactionTypes:
                self.inventory_repo.persistTransactionType(transactionType)
        except HTTPException as e:
            raise BAD_REQUEST(e.detail)
        return

    def updateInventoryItem(self,id:int,inventoryItem) -> None:
        if self.inventory_repo.getInventoryItemBySalesServiceItemId(inventoryItem.sales_service_item_id) and id != self.inventory_repo.getInventoryItemBySalesServiceItemId(inventoryItem.sales_service_item_id).id:
            
            raise BAD_REQUEST("Sales Item already in use.")
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