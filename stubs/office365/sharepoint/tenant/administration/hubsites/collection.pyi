from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.paths.service_operation import (
    ServiceOperationPath as ServiceOperationPath,
)
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection
from office365.sharepoint.tenant.administration.hubsites.hub_site import (
    HubSite as HubSite,
)

class HubSiteCollection(EntityCollection[HubSite]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def get_by_id(self, _id): ...
    def get_connected_hubs(self, hub_site_id, option): ...
    def get_site_url_by_hub_site_id(self, hub_site_id): ...
