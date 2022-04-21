from pydantic import BaseModel
from typing import Optional, List

class BulkDelete(BaseModel):
    listOfId : Optional[List[int]] = []
