from _typeshed import Incomplete
from office365.directory.identitygovernance.privilegedaccess.unified_role_assignment_schedule_request import (
    UnifiedRoleAssignmentScheduleRequest as UnifiedRoleAssignmentScheduleRequest,
)
from office365.directory.rolemanagement.unifiedrole.assignment import (
    UnifiedRoleAssignment as UnifiedRoleAssignment,
)
from office365.directory.rolemanagement.unifiedrole.definition import (
    UnifiedRoleDefinition as UnifiedRoleDefinition,
)
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class RbacApplication(Entity):
    @property
    def role_assignments(self) -> EntityCollection[UnifiedRoleAssignment]: ...
    @property
    def role_definitions(self) -> EntityCollection[UnifiedRoleDefinition]: ...
    def role_assignment_schedule_requests(
        self,
    ) -> EntityCollection[UnifiedRoleAssignmentScheduleRequest]: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
