from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.sharepoint.directory.group import Group as Group
from office365.sharepoint.entity import Entity as Entity

class GroupAndUserStatus(Entity):
    @property
    def group(self): ...
    @property
    def entity_type_name(self): ...
