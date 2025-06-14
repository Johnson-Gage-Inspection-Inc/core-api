from _typeshed import Incomplete
from office365.directory.object import DirectoryObject as DirectoryObject
from office365.directory.object_collection import (
    DirectoryObjectCollection as DirectoryObjectCollection,
)
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class OrgContact(DirectoryObject):
    @property
    def direct_reports(self): ...
    @property
    def manager(self): ...
    @property
    def member_of(self): ...
    @property
    def transitive_member_of(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
