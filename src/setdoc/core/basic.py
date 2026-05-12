from typing import TypeVar

from setdoc.core.getbasicdoc import getbasicdoc
from setdoc.typing.SupportsDocAndName import SupportsDocAndName

__all__ = ["basic"]

Value = TypeVar("Value", bound=SupportsDocAndName)


def basic(value: Value) -> Value:
    "This decorator sets the docstring of the given value to what is suggested by its name."
    value.__doc__ = getbasicdoc(value.__name__)
    return value
