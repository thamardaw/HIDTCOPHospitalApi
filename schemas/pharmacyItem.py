from pydantic import BaseModel


class PharmacyItem(BaseModel):
    category_id : int
    brand_name : str
    generic_name : str
    form : str
    strength : str
    unit : str
    po_unit : str
    converstion_rate : int