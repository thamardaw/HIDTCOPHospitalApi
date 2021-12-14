from sqlalchemy import Column, Integer, String, Enum
from infrastructure.base_mixin import BaseMixin
from sqlalchemy.sql.schema import ForeignKey
from infrastructure.base_class import Base

class BillItem(BaseMixin,Base):
    patient_id = Column(Integer,ForeignKey("patient.id"))
    sales_service_item_id = Column(Integer,ForeignKey("salesserviceitem.id"))
    name = Column(String, nullable=False)
    quantity = Column(Integer,nullable=False)
    uom = Column(String)
    price = Column(Integer,nullable=False)
    subtotal = Column(Integer,nullable=False)
    remark = Column(String, nullable=False)