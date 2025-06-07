from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class ContentTypeCreationInformation(ClientValue):
    Name: Incomplete
    Description: Incomplete
    group: Incomplete
    Id: Incomplete
    def __init__(
        self,
        name,
        description: Incomplete | None = None,
        group: Incomplete | None = None,
        ct_id: Incomplete | None = None,
    ) -> None: ...
