from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class SecondaryAdministratorsInfo(ClientValue):
    email: Incomplete
    loginName: Incomplete
    userPrincipalName: Incomplete
    def __init__(
        self,
        email: Incomplete | None = None,
        loginName: Incomplete | None = None,
        userPrincipalName: Incomplete | None = None,
    ) -> None: ...
    @property
    def entity_type_name(self) -> str: ...
