from _typeshed import Incomplete
from office365.directory.applications.roles.assignment import AppRoleAssignment as AppRoleAssignment
from office365.entity_collection import EntityCollection as EntityCollection

class AppRoleAssignmentCollection(EntityCollection[AppRoleAssignment]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
