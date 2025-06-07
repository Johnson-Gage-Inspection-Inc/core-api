from office365.directory.identitygovernance.privilegedaccess.group import PrivilegedAccessGroup as PrivilegedAccessGroup
from office365.entity import Entity as Entity
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class PrivilegedAccessRoot(Entity):
    @property
    def group(self): ...
