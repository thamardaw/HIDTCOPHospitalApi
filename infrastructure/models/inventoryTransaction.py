from sqlalchemy import Column, Integer, String, Date
from infrastructure.base_mixin import BaseMixin
from sqlalchemy.sql.schema import ForeignKey
from infrastructure.base_class import Base
from sqlalchemy.orm import relationship

class InventoryTransaction(BaseMixin,Base):
    inventory_item_id = Column(Integer,ForeignKey("inventoryitem.id"))
    inventory_item = relationship("InventoryItem",backref="inventorytransaction")
    inventory_item_name = Column(String,nullable=False)
    transaction_type_name = Column(String,nullable=False)
    quantity = Column(Integer,nullable=False)
    opening_balance = Column(Integer,nullable=False)
    closing_balance = Column(Integer,nullable=False)
    unit = Column(String,nullable=False)
    purchasing_price = Column(Integer,nullable=False)
    selling_price = Column(Integer,nullable=False)
    note = Column(String)