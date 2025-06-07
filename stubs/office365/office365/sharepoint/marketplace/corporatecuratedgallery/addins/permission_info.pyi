from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class SPAddinPermissionInfo(ClientValue):
    absoluteUrl: Incomplete
    def __init__(self, absolute_url: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
