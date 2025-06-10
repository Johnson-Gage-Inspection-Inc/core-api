from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class VersionFacet(ClientValue):
    fromVersion: Incomplete
    def __init__(self, fromVersion: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
