from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection
from office365.sharepoint.tenant.administration.site_user_group_info import (
    SiteUserGroupInfo as SiteUserGroupInfo,
)
from office365.sharepoint.tenant.administration.sites.properties import (
    SiteProperties as SiteProperties,
)
from office365.sharepoint.tenant.administration.sites.state_properties import (
    SiteStateProperties as SiteStateProperties,
)

class SitePropertiesCollection(EntityCollection[SiteProperties]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def get_by_id(self, site_id): ...
    def get_lock_state_by_id(self, site_id): ...
    def get_site_state_properties(self, site_id): ...
    def get_site_user_groups(self, site_id): ...
    def check_site_is_archived_by_id(self, site_id): ...
