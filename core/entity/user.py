from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    password: str
    role: str
    class Config():
        orm_mode = True

class Username(BaseModel):
    username: str
    class Config():
        orm_mode = True