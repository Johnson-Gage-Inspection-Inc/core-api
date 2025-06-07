from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class TrackedItemUpdatesRequest(ClientValue):
    TimeStamp: Incomplete
    TrackedItemsAsJson: Incomplete
    def __init__(self, timestamp: Incomplete | None = None, tracked_items_as_json: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
