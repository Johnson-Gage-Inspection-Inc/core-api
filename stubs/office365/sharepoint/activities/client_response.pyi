from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class ActivityClientResponse(ClientValue):
    id: Incomplete
    message: Incomplete
    serverId: Incomplete
    status: Incomplete
    def __init__(
        self, id_: str, message: str = None, server_id: str = None, status: int = None
    ) -> None: ...
    @property
    def entity_type_name(self): ...
