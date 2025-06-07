from office365.directory.rolemanagement.application import RbacApplication as RbacApplication
from office365.entity import Entity as Entity
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class RoleManagement(Entity):
    @property
    def directory(self): ...
    @property
    def entitlement_management(self): ...
