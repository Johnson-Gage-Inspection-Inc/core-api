from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.logger.logFileInfoCollection import (
    LogFileInfoCollection as LogFileInfoCollection,
)

class LogExport(Entity):
    def __init__(self, context) -> None: ...
    def get_files(self): ...
    def get_log_types(self): ...
    @property
    def entity_type_name(self): ...
