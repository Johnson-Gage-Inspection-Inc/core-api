from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class HubSitePermission(ClientValue):
    DisplayName: Incomplete
    PrincipalName: Incomplete
    Rights: Incomplete
    def __init__(self, display_name: Incomplete | None = None, principal_name: Incomplete | None = None, rights: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
