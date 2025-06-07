from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class UserDirectoryInfo(ClientValue):
    Name: Incomplete
    NetId: Incomplete
    PrimaryEmail: Incomplete
    PrincipalName: Incomplete
    def __init__(
        self,
        name: Incomplete | None = None,
        net_id: Incomplete | None = None,
        primary_email: Incomplete | None = None,
        principal_name: Incomplete | None = None,
    ) -> None: ...
    @property
    def entity_type_name(self): ...
