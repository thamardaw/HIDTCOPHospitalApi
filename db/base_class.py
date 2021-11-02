from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy import Column,Integer

@as_declarative()
class Base:
    id=Column(Integer, index=True, autoincrement=True, primary_key=True)

    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()