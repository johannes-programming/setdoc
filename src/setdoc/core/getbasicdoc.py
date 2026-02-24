from typing import *

from setdoc._utils import Cfg

__all__ = ["getbasicdoc"]


def getbasicdoc(name: str) -> str:
    "This function returns the basic docstring for a given name."
    return Cfg.cfg.data["basic"][name]
