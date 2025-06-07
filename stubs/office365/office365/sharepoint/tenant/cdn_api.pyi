from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.tenant.cdn_url import TenantCdnUrl as TenantCdnUrl

class TenantCdnApi(Entity):
    def __init__(self, context) -> None: ...
    def get_cdn_urls(self, items: Incomplete | None = None): ...
    @property
    def entity_type_name(self): ...
