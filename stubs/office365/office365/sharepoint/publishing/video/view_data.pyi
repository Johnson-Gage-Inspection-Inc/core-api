from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class ViewData(ClientValue):
    TotalHits: Incomplete
    TotalUsers: Incomplete
    def __init__(
        self,
        total_hits: Incomplete | None = None,
        total_users: Incomplete | None = None,
    ) -> None: ...
    @property
    def entity_type_name(self): ...
