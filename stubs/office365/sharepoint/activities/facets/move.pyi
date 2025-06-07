from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class MoveFacet(ClientValue):
    from_: Incomplete
    to: Incomplete
    def __init__(self, from_=..., to=...) -> None: ...
    @property
    def entity_type_name(self): ...
