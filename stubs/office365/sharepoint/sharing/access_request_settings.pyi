from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class AccessRequestSettings(ClientValue):
    hasPendingAccessRequests: Incomplete
    pendingAccessRequestsLink: Incomplete
    requiresAccessApproval: Incomplete
    def __init__(self, has_pending_access_requests: Incomplete | None = None, pending_access_requests_link: Incomplete | None = None, requires_access_approval: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
