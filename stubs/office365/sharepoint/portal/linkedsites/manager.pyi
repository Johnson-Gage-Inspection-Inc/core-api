from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.portal.linkedsites.list_contract import (
    LinkedSitesListContract as LinkedSitesListContract,
)

class SiteLinkingManager(Entity):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def get_site_links(self): ...
    @property
    def entity_type_name(self): ...
