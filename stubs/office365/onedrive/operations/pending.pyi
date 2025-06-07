from _typeshed import Incomplete
from office365.onedrive.operations.pending_content_update import PendingContentUpdate as PendingContentUpdate
from office365.runtime.client_value import ClientValue as ClientValue

class PendingOperations(ClientValue):
    pendingContentUpdate: Incomplete
    def __init__(self, pending_content_update=...) -> None: ...
