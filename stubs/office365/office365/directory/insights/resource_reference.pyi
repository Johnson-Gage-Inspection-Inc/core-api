from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class ResourceReference(ClientValue):
    id: Incomplete
    type: Incomplete
    webUrl: Incomplete
    def __init__(
        self,
        _id: Incomplete | None = None,
        _type: Incomplete | None = None,
        web_url: Incomplete | None = None,
    ) -> None: ...
