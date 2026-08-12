from setdoc.core.basic import basic
from setdoc.core.Basics import Basics
from setdoc.core.getbasicdoc import getbasicdoc
from setdoc.core.SetDoc import SetDoc

__all__ = ["Basics", "SetDoc", "basic", "getbasicdoc", "setdoc"]

setdoc: type[SetDoc] = SetDoc  # legacy
