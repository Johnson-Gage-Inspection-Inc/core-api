from _typeshed import Incomplete
from office365.delta_collection import DeltaCollection as DeltaCollection
from office365.directory.groups.group import Group as Group
from office365.directory.groups.profile import GroupProfile as GroupProfile
from office365.runtime.queries.create_entity import (
    CreateEntityQuery as CreateEntityQuery,
)

class GroupCollection(DeltaCollection[Group]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def add(self, group_properties): ...
    def create_m365(
        self,
        name,
        description: Incomplete | None = None,
        owner: Incomplete | None = None,
    ): ...
    def create_security(self, name, description: Incomplete | None = None): ...
    def create_with_team(self, group_name): ...
    def get_by_name(self, name: str) -> Group: ...
