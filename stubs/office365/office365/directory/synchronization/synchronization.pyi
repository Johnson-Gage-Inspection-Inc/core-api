from office365.directory.synchronization.job import (
    SynchronizationJob as SynchronizationJob,
)
from office365.directory.synchronization.template import (
    SynchronizationTemplate as SynchronizationTemplate,
)
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class Synchronization(Entity):
    @property
    def jobs(self) -> EntityCollection[SynchronizationJob]: ...
    @property
    def templates(self) -> EntityCollection[SynchronizationTemplate]: ...
