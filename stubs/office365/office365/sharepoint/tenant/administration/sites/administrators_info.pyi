from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class SiteAdministratorsInfo(ClientValue):
    email: Incomplete
    loginName: Incomplete
    name: Incomplete
    def __init__(
        self,
        email: Incomplete | None = None,
        login_name: Incomplete | None = None,
        name: Incomplete | None = None,
    ) -> None: ...
    @property
    def entity_type_name(self): ...
