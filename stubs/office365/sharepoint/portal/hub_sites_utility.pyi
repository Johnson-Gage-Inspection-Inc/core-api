from _typeshed import Incomplete
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.tenant.administration.hubsites.collection import HubSiteCollection as HubSiteCollection

class SPHubSitesUtility(Entity):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def get_hub_sites(self): ...
