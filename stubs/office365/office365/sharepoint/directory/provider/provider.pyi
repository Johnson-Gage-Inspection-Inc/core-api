from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.directory.provider.object_data import (
    DirectoryObjectData as DirectoryObjectData,
)
from office365.sharepoint.entity import Entity as Entity

class SharePointDirectoryProvider(Entity):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def check_site_availability(self, site_url): ...
    def read_directory_object(
        self, data: DirectoryObjectData
    ) -> ClientResult[DirectoryObjectData]: ...
    @property
    def entity_type_name(self): ...
