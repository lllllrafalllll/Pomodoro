from sqlalchemy.orm import  DeclarativeBase, declared_attr
from typing import Any


class Base(DeclarativeBase):
    id: Any
    __name__: str


    __allow__unmapped__ = True

    @declared_attr
    def __tablename__(self) -> str:
        return self.__name__.lower()