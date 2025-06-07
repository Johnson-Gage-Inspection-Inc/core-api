from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.sites.manager.types import (
    TopSiteFilesResult as TopSiteFilesResult,
)

class SiteManagerService(Entity):
    def __init__(self, context) -> None: ...
    def top_files(self, max_count: Incomplete | None = None): ...
    @property
    def entity_type_name(self): ...
