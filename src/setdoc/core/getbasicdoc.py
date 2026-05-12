from typing import Optional, cast

from setdoc._utils import Cfg

__all__ = ["getbasicdoc"]


def getbasicdoc(name: str) -> Optional[str]:
    "This function returns the basic docstring for a given name."
    return cast(Optional[str], Cfg.cfg.basic.get(name))
