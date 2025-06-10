from _typeshed import Incomplete
from office365.entity_collection import EntityCollection as EntityCollection
from office365.onedrive.termstore.sets.name import LocalizedName as LocalizedName
from office365.onedrive.termstore.sets.set import Set as Set
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.queries.create_entity import (
    CreateEntityQuery as CreateEntityQuery,
)

class SetCollection(EntityCollection[Set]):
    def __init__(
        self,
        context,
        resource_path: Incomplete | None = None,
        parent_group: Incomplete | None = None,
    ) -> None: ...
    def get_by_name(self, name: str) -> Set: ...
    def add(self, name, parent_group: Incomplete | None = None): ...
