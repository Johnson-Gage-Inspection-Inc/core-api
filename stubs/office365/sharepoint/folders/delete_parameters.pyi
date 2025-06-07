from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class FolderDeleteParameters(ClientValue):
    BypassSharedLock: Incomplete
    DeleteIfEmpty: Incomplete
    ETagMatch: Incomplete
    def __init__(self, bypass_shared_lock: Incomplete | None = None, delete_if_empty: Incomplete | None = None, etag_match: Incomplete | None = None) -> None: ...
