from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class NavigationNodeCreationInformation(ClientValue):
    Title: Incomplete
    Url: Incomplete
    IsExternal: Incomplete
    AsLastNode: Incomplete
    PreviousNode: Incomplete
    def __init__(self, title: Incomplete | None = None, url: Incomplete | None = None, is_external: bool = False, as_last_node: bool = False, previous_node: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
