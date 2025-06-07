from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity

class RecentFileCollection(Entity):
    def __init__(self, context) -> None: ...
    @staticmethod
    def get_recent_files(context, top): ...
