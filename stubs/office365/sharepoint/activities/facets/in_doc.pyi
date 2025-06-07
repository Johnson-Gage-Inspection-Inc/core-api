from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class InDocFacet(ClientValue):
    contentId: Incomplete
    navigationId: Incomplete
    def __init__(self, contentId: Incomplete | None = None, navigationId: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
