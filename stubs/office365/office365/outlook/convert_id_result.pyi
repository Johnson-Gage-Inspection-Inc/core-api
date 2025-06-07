from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class ConvertIdResult(ClientValue):
    sourceId: Incomplete
    targetId: Incomplete
    def __init__(
        self, source_id: Incomplete | None = None, target_id: Incomplete | None = None
    ) -> None: ...
