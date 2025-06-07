from _typeshed import Incomplete
from office365.directory.rolemanagement.unifiedrole.permission import UnifiedRolePermission as UnifiedRolePermission
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class UnifiedRoleDefinition(Entity):
    @property
    def display_name(self) -> str | None: ...
    @property
    def is_built_in(self) -> bool | None: ...
    @property
    def role_permissions(self) -> ClientValueCollection[UnifiedRolePermission]: ...
    @property
    def inherits_permissions_from(self) -> EntityCollection[UnifiedRoleDefinition]: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
