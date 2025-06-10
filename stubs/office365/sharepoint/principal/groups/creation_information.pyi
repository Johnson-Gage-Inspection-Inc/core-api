from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class GroupCreationInformation(ClientValue):
    Title: Incomplete
    Description: Incomplete
    def __init__(
        self, title: Incomplete | None = None, description: Incomplete | None = None
    ) -> None: ...
    @property
    def entity_type_name(self): ...
