from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.sharepoint.sharing.principal import Principal as Principal

class LinkInvitation(ClientValue):
    invitedBy: Incomplete
    invitedOn: Incomplete
    invitee: Incomplete
    def __init__(
        self, invited_by=..., invited_on: Incomplete | None = None, invitee=...
    ) -> None: ...
    @property
    def entity_type_name(self): ...
