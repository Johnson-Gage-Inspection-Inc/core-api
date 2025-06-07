from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class ListItemUpdateParameters(ClientValue):
    BypassQuotaCheck: Incomplete
    BypassSharedLock: Incomplete
    def __init__(self, bypass_quota_check: Incomplete | None = None, bypass_shared_lock: Incomplete | None = None) -> None: ...
