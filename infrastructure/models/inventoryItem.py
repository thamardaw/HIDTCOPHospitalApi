from sqlalchemy import Column, Integer, String, Date
from infrastructure.base_mixin import BaseMixin
from sqlalchemy.sql.schema import ForeignKey
from infrastructure.base_class import Base
from sqlalchemy.orm import relationship

class InventoryItem(BaseMixin,Base):
    pharmacy_item_id = Column(Integer,ForeignKey("pharmacyitem.id"))
    pharmacy_item = relationship("PharmacyItem",backref="inventoryitem")
    name = Column(String,nullable=False)
    balance = Column(Integer,nullable=False)
    unit = Column(String,nullable=False)
    purchasing_price = Column(Integer,nullable=False)
    sales_service_item_id = Column(Integer,ForeignKey("salesserviceitem.id"))
    sales_service_item = relationship("SalesServiceItem",backref="inventoryitem")
    expiry_date = Column(Date)
    batch = Column(String,nullable=False)