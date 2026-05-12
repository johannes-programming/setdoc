from typing import Optional, Protocol

__all__ = ["SupportsDocAndName"]


class SupportsDocAndName(Protocol):
    __doc__: Optional[str]
    __name__: str
