from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class WorkbookSessionInfo(ClientValue):
    persistChanges: Incomplete
    id: Incomplete
    def __init__(
        self,
        session_id: Incomplete | None = None,
        persist_changes: Incomplete | None = None,
    ) -> None: ...
