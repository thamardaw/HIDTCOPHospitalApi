from typing import Protocol

class UserProtocol(Protocol):
    def persist(self,user):
        ...

    def update(self,username,data):
        ...
        
    def readByUsername(self,username):
        ...