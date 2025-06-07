from office365.directory.synchronization.schema import (
    SynchronizationSchema as SynchronizationSchema,
)
from office365.entity import Entity as Entity
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class SynchronizationTemplate(Entity):
    @property
    def schema(self): ...
