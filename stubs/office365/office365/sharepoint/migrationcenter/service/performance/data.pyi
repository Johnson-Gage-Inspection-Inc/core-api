from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection
from office365.sharepoint.migrationcenter.service.performance.dashboard_data import (
    PerformanceDashboardData as PerformanceDashboardData,
)
from office365.sharepoint.migrationcenter.service.performance.entity_data import (
    MigrationPerformanceEntityData as MigrationPerformanceEntityData,
)

class PerformanceData(MigrationPerformanceEntityData):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...

class PerformanceDataCollection(EntityCollection[PerformanceData]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def get_data(
        self,
        start_time: Incomplete | None = None,
        end_time: Incomplete | None = None,
        agent_id: Incomplete | None = None,
        time_unit: Incomplete | None = None,
    ): ...
