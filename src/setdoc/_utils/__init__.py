import enum
import functools
import tomllib
from importlib import resources
from typing import Any, Self, cast

__all__ = ["Cfg"]


class Cfg(enum.Enum):
    cfg = None

    @functools.cached_property
    def basic(self: Self) -> dict[str, Any]:
        return cast(dict[str, Any], self.data["basic"])

    @functools.cached_property
    def data(self: Self) -> dict[str, Any]:
        "This cached property holds the cfg data."
        text: str
        text = resources.read_text("setdoc._utils", "cfg.toml")
        return tomllib.loads(text)
