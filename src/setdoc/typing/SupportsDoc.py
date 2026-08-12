from typing import Protocol

__all__ = ["SupportsDoc"]


class SupportsDoc(Protocol):
    __doc__: str | None
