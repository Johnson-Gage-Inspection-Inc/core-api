from office365.directory.object import DirectoryObject as DirectoryObject
from office365.directory.permissions.scoped_role_membership import ScopedRoleMembership as ScopedRoleMembership
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class DirectoryRole(DirectoryObject):
    @property
    def description(self) -> str | None: ...
    @property
    def display_name(self) -> str | None: ...
    @property
    def members(self): ...
    @property
    def scoped_members(self): ...
