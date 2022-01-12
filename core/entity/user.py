from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    role: str
    class Config():
        orm_mode = True