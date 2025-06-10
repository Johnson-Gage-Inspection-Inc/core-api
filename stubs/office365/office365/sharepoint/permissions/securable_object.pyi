from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.permissions.base_permissions import (
    BasePermissions as BasePermissions,
)
from office365.sharepoint.permissions.roles.assignments.assignment import (
    RoleAssignment as RoleAssignment,
)
from office365.sharepoint.permissions.roles.assignments.collection import (
    RoleAssignmentCollection as RoleAssignmentCollection,
)
from office365.sharepoint.permissions.roles.definitions.definition import (
    RoleDefinition as RoleDefinition,
)
from office365.sharepoint.principal.principal import Principal as Principal
from office365.sharepoint.principal.users.user import User as User
from typing_extensions import Self

class SecurableObject(Entity):
    def get_role_assignment(self, principal): ...
    def add_role_assignment(
        self, principal: Principal | str, role: RoleDefinition | int
    ) -> Self: ...
    def remove_role_assignment(
        self, principal: Principal | str, role_def: RoleDefinition | int
    ) -> Self: ...
    def break_role_inheritance(
        self, copy_role_assignments: bool = True, clear_sub_scopes: bool = True
    ): ...
    def reset_role_inheritance(self): ...
    def get_user_effective_permissions(
        self, user: str | User
    ) -> ClientResult[BasePermissions]: ...
    @property
    def has_unique_role_assignments(self) -> bool | None: ...
    @property
    def first_unique_ancestor_securable_object(self) -> SecurableObject: ...
    @property
    def role_assignments(self) -> RoleAssignmentCollection: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
