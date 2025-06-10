from _typeshed import Incomplete
from office365.sharepoint.changes.change import Change as Change
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection

class ChangeCollection(EntityCollection[Change]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def set_property(self, key, value, persist_changes: bool = False) -> None: ...
