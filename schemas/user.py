from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    role: str

class ResetPassword(BaseModel):
    username: str
    oldPassword:str
    newPassword:str
