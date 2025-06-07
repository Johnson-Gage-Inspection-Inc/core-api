from office365.directory.synchronization.schema import (
    SynchronizationSchema as SynchronizationSchema,
)
from office365.directory.synchronization.status import (
    SynchronizationStatus as SynchronizationStatus,
)
from office365.entity import Entity as Entity
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)

class SynchronizationJob(Entity):
    def pause(self): ...
    def start(self): ...
    @property
    def status(self): ...
    @property
    def schema(self): ...
