from sqlalchemy import Column, Integer, String, Date, Boolean
from infrastructure.base_mixin import BaseMixin
# from sqlalchemy.sql.schema import ForeignKey
from infrastructure.base_class import Base
from sqlalchemy.orm import relationship

class InventoryItem(BaseMixin,Base):
    # pharmacy_item_id = Column(Integer,ForeignKey("pharmacyitem.id"))
    # pharmacy_item = relationship("PharmacyItem",backref="inventoryitem")
    name = Column(String,nullable=False)
    balance = Column(Integer,nullable=False)
    unit = Column(String,nullable=False)
    purchasing_price = Column(Integer,nullable=False)
    sales_service_item_id = Column(Integer,index=True)
    expiry_date = Column(Date)
    batch = Column(String,nullable=False)
    is_active = Column(Boolean,nullable=False,server_default="true")
    
    sales_service_item = relationship('SalesServiceItem', primaryjoin="InventoryItem.sales_service_item_id==foreign(SalesServiceItem.id)",uselist=False)
    inventory_transaction= relationship("InventoryTransaction",back_populates="inventory_item")