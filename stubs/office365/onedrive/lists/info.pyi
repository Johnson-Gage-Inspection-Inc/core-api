from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class ListInfo(ClientValue):
    template: Incomplete
    contentTypesEnabled: Incomplete
    hidden: Incomplete
    def __init__(
        self,
        template: Incomplete | None = None,
        content_types_enabled: bool = False,
        hidden: bool = False,
    ) -> None: ...
