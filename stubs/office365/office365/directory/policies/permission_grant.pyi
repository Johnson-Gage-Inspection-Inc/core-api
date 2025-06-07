from office365.directory.permissions.grants.condition_set import (
    PermissionGrantConditionSet as PermissionGrantConditionSet,
)
from office365.directory.policies.base import PolicyBase as PolicyBase
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class PermissionGrantPolicy(PolicyBase):
    @property
    def excludes(self) -> EntityCollection[PermissionGrantConditionSet]: ...
    @property
    def includes(self) -> EntityCollection[PermissionGrantConditionSet]: ...
