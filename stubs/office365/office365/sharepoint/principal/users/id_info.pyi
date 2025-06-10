from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class UserIdInfo(ClientValue):
    NameId: Incomplete
    NameIdIssuer: Incomplete
    def __init__(
        self,
        name_id: Incomplete | None = None,
        name_id_issuer: Incomplete | None = None,
    ) -> None: ...
