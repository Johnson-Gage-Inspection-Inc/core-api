from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.types.collections import StringCollection as StringCollection

class ResourceAction(ClientValue):
    allowedResourceActions: Incomplete
    notAllowedResourceActions: Incomplete
    def __init__(self, allowed: Incomplete | None = None, not_allowed: Incomplete | None = None) -> None: ...
