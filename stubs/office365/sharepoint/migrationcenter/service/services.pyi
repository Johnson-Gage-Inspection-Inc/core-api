from _typeshed import Incomplete
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.migrationcenter.service.performance.data import (
    PerformanceDataCollection as PerformanceDataCollection,
)
from office365.sharepoint.migrationcenter.service.teams import (
    MigrationCenterTeams as MigrationCenterTeams,
)

class MigrationCenterServices(Entity):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    @property
    def performance_data(self) -> PerformanceDataCollection: ...
    @property
    def teams(self) -> PerformanceDataCollection: ...
    @property
    def entity_type_name(self): ...
