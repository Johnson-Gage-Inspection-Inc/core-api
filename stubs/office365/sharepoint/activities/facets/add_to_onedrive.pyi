from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class AddToOneDriveFacet(ClientValue):
    addedDateTime: Incomplete
    mountPointName: Incomplete
    removedDateTime: Incomplete
    def __init__(self, added_datetime: Incomplete | None = None, mount_point_name: Incomplete | None = None, removed_datetime: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
