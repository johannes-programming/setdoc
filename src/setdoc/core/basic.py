from typing import *

from setdoc.core.getbasicdoc import getbasicdoc

__all__ = ["basic"]


def basic(value: Any) -> Any:
    "This decorator sets the docstring of the given value to what is suggested by its name."
    value.__doc__ = getbasicdoc(value.__name__)
    return value
