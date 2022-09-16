from typing import Protocol, List
from core.entity.user import User as UserDTO, PublicUser as PublicUserDTO 

class UserProtocol(Protocol):
    def list(self) -> List[PublicUserDTO]:
        ...
    
    def getById(self,id: int) -> PublicUserDTO:
        ...

    def persist(self,user) -> UserDTO:
        ...

    def updateByUsername(self,username,data) -> None:
        ...

    def update(self,id,data) -> None:
        ...
        
    def readByUsername(self,username: str) -> UserDTO:
        ...