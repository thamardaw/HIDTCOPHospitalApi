from sqlalchemy import Column, Integer, String, Enum
from infrastructure.base_mixin import BaseMixin
from sqlalchemy.sql.schema import ForeignKey
from infrastructure.base_class import Base
from sqlalchemy.orm import relationship

class BillItem(BaseMixin,Base):
    bill_id = Column(Integer,ForeignKey("bill.id"))
    bill = relationship("Bill",back_populates="bill_items")
    sales_service_item_id = Column(Integer,ForeignKey("salesserviceitem.id"))
    name = Column(String, nullable=False)
    quantity = Column(Integer,nullable=False)
    uom = Column(String)
    price = Column(Integer,nullable=False)
    subtotal = Column(Integer,nullable=False)
    remark = Column(String)