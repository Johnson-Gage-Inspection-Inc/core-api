from _typeshed import Incomplete
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection
from office365.sharepoint.multigeo.storage_quota import StorageQuota as StorageQuota
from office365.sharepoint.multigeo.unified_group import UnifiedGroup as UnifiedGroup
from office365.sharepoint.multigeo.user_personal_site_location import (
    UserPersonalSiteLocation as UserPersonalSiteLocation,
)

class MultiGeoServices(Entity):
    def __init__(self, context) -> None: ...
    def user_personal_site_location(
        self, user_principal_name: str
    ) -> UserPersonalSiteLocation: ...
    @property
    def storage_quotas(self) -> EntityCollection[UnifiedGroup]: ...
    @property
    def unified_groups(self) -> EntityCollection[UnifiedGroup]: ...
    @property
    def entity_type_name(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
