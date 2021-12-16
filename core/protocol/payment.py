from typing import Protocol

class BillProtocol(Protocol):
    def persist(self,data):
        ...

    def list(self):
        ...