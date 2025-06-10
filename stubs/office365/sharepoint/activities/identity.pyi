from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.sharepoint.activities.identity_item import (
    ActivityIdentityItem as ActivityIdentityItem,
)

class ActivityIdentity(ClientValue):
    clientId: Incomplete
    group: Incomplete
    user: Incomplete
    def __init__(
        self, client_id: Incomplete | None = None, group=..., user=...
    ) -> None: ...
    @property
    def entity_type_name(self): ...
