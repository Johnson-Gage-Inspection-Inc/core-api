from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.tenant.administration.hubsites.permission import (
    HubSitePermission as HubSitePermission,
)

class HubSiteProperties(Entity):
    @property
    def permissions(self): ...
    @property
    def site_id(self) -> str | None: ...
    @property
    def property_ref_name(self): ...
    @property
    def entity_type_name(self): ...
