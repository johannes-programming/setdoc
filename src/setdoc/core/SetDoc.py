import dataclasses
from typing import Optional, Self, TypeVar

from setdoc.typing.SupportsDoc import SupportsDoc

__all__ = ["SetDoc"]

Target = TypeVar("Target", bound=SupportsDoc)


@dataclasses.dataclass
class SetDoc:
    "This class helps to set doc strings."

    doc: Optional[str]

    def __call__(self: Self, target: Target) -> Target:
        "This magic method implements calling the current instance. It sets the doc string of the passed target to the value stored in the doc field of the setdoc object."
        target.__doc__ = self.doc
        return target
