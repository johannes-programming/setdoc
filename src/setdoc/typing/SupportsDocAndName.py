from typing import Protocol

__all__ = ["SupportsDocAndName"]


class SupportsDocAndName(Protocol):
    __doc__: str | None
    __name__: str
