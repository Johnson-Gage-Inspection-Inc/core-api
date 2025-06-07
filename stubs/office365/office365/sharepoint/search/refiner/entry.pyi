from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class RefinerEntry(ClientValue):
    RefinementCount: Incomplete
    RefinementName: Incomplete
    def __init__(
        self,
        refinement_count: Incomplete | None = None,
        refinement_name: Incomplete | None = None,
    ) -> None: ...
    @property
    def entity_type_name(self): ...
