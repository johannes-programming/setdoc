import dataclasses
from typing import *

__all__ = ["setdoc"]


@dataclasses.dataclass
class setdoc:
    "This class helps to set doc strings."

    doc: Any

    def __call__(self, target: Any) -> Any:
        "This magic method implements calling the current instance. It sets the doc string of the passed target to the value stored in the doc field of the setdoc object."
        target.__doc__ = self.doc
        return target
