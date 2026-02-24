from setdoc.core.basic import basic
from typing import *

__all__ = ["Basic"]


class Basics:
    __slots__ = ("names",)

    names:tuple[str, ...]

    def __call__(self:Self, cls:Any, /) -> Any:
        x:str
        y:Any
        for x in self.names:
            y=getattr(cls, x)
            basic(y)
        return cls
            
    @basic
    def __init__(self:Self, *names:str)->None:
        self.names = names