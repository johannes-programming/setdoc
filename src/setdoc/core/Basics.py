import dataclasses
import inspect as ins
from typing import Self

from setdoc.core.basic import basic
from setdoc.core.getbasicdoc import getbasicdoc

__all__ = ["Basics"]


@dataclasses.dataclass()
class Basics:
    """Try setting doc-string by __name__ for the args, by keyword for the kwargs."""

    excepts: tuple[type[BaseException], ...] = dataclasses.field(
        default=(),
        kw_only=True,
    )

    @basic
    def __call__(self: Self, /, *args: object, **kwargs: object) -> None:
        x: str
        y: object
        for y in args:
            try:
                x = y.__name__  # type: ignore[attr-defined]
                unwrapped = ins.unwrap(y)
                unwrapped.__doc__ = getbasicdoc(x)
            except self.excepts:
                pass
        for x, y in kwargs.items():
            try:
                unwrapped = ins.unwrap(y)
                unwrapped.__doc__ = getbasicdoc(x)
            except self.excepts:
                pass
