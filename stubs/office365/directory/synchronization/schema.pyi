from office365.directory.synchronization.directory_definition import (
    DirectoryDefinition as DirectoryDefinition,
)
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class SynchronizationSchema(Entity):
    @property
    def directories(self) -> EntityCollection[DirectoryDefinition]: ...
