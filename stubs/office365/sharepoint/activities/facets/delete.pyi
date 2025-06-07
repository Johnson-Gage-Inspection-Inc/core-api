from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class DeleteFacet(ClientValue):
    name: Incomplete
    def __init__(self, name: str = None) -> None: ...
    @property
    def entity_type_name(self): ...
