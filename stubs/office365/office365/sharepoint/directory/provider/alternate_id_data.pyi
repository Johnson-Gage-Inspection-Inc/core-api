from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class AlternateIdData(ClientValue):
    Email: Incomplete
    IdentifyingProperty: Incomplete
    UserPrincipalName: Incomplete
    def __init__(
        self,
        email: Incomplete | None = None,
        identifying_property: Incomplete | None = None,
        user_principal_name: Incomplete | None = None,
    ) -> None: ...
    @property
    def entity_type_name(self): ...
