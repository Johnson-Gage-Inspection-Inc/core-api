from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.orgnewssite.info import OrgNewsSiteInfo as OrgNewsSiteInfo

class OrgNewsSiteApi(Entity):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def details(self): ...
    @property
    def entity_type_name(self): ...
