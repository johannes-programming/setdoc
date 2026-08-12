from setdoc._utils import Cfg

__all__ = ["getbasicdoc"]


def getbasicdoc(name: str) -> str | None:
    "This function returns the basic docstring for a given name."
    return Cfg.cfg.basic.get(name)
