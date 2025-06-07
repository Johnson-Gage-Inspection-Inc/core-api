from _typeshed import Incomplete
from office365.directory.object_collection import DirectoryObjectCollection as DirectoryObjectCollection
from office365.directory.policies.base import PolicyBase as PolicyBase
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class AppManagementPolicy(PolicyBase):
    @property
    def applies_to(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
