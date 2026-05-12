from typing import Optional, Protocol

__all__ = ["SupportsDoc"]


class SupportsDoc(Protocol):
    __doc__: Optional[str]
