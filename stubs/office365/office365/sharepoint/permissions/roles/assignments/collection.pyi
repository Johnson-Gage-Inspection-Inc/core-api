from _typeshed import Incomplete
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.paths.service_operation import (
    ServiceOperationPath as ServiceOperationPath,
)
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection
from office365.sharepoint.permissions.roles.assignments.assignment import (
    RoleAssignment as RoleAssignment,
)

class RoleAssignmentCollection(EntityCollection[RoleAssignment]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def __getitem__(self, key): ...
    def get_by_principal_id(self, principal_id): ...
    def add_role_assignment(self, principal_id, role_def_id): ...
    def remove_role_assignment(self, principal_id, role_def_id): ...
