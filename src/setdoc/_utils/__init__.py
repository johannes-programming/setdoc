import enum
import functools
import tomllib
from importlib import resources
from typing import *

__all__ = ["Cfg"]

class Cfg(enum.Enum):
    cfg = None

    @functools.cached_property
    def data(self: Self) -> dict:
        "This cached property holds the cfg data."
        text: str
        text = resources.read_text("setdoc._uitls", "cfg.toml")
        return tomllib.loads(text)
