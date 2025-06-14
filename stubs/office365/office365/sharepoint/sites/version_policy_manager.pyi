from _typeshed import Incomplete
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.lists.version_policy_manager import (
    VersionPolicyManager as VersionPolicyManager,
)

class SiteVersionPolicyManager(Entity):
    @property
    def major_version_limit(self) -> int | None: ...
    @property
    def version_policies(self): ...
    def inherit_tenant_settings(self): ...
    def set_auto_expiration(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
