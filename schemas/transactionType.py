from pydantic import BaseModel
from infrastructure.models.transactionType import type_enum

class TransactionType(BaseModel):
    name: str
    type: type_enum