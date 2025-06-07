from office365.directory.identitygovernance.privilegedaccess.approval import Approval as Approval
from office365.directory.identitygovernance.privilegedaccess.schedule.group_assignment_instance import PrivilegedAccessGroupAssignmentScheduleInstance as PrivilegedAccessGroupAssignmentScheduleInstance
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class PrivilegedAccessGroup(Entity):
    @property
    def assignment_approvals(self): ...
    @property
    def assignment_schedule_instances(self): ...
