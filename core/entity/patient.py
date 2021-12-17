from datetime import date
from typing import Any, Optional
from pydantic import BaseModel
from datetime import datetime
from infrastructure.models.patient import gender_enum

class Patient(BaseModel):
    id: int
    name: str
    gender: gender_enum
    date_of_birth: date
    age: int
    address: str
    contact_details: str
    created_time: Optional[datetime] = None
    updated_time: Optional[datetime] = None
    created_user_id: Optional[int] = None
    updated_user_id: Optional[int] = None
    class Config():
        orm_mode = True
