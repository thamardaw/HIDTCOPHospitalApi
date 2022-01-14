from pydantic import BaseModel

class Uom(BaseModel):
    name: str
    description: str
