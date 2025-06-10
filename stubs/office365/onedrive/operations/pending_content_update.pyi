from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class PendingContentUpdate(ClientValue):
    queuedDateTime: Incomplete
    def __init__(self, queued_datetime: Incomplete | None = None) -> None: ...
