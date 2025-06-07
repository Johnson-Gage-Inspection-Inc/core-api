from _typeshed import Incomplete
from office365.directory.object_collection import (
    DirectoryObjectCollection as DirectoryObjectCollection,
)
from office365.entity import Entity as Entity
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class FeatureRolloutPolicy(Entity):
    @property
    def applies_to(self) -> DirectoryObjectCollection: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
