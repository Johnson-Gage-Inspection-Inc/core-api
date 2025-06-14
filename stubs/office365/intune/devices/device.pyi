from _typeshed import Incomplete
from office365.directory.object import DirectoryObject as DirectoryObject
from office365.directory.object_collection import (
    DirectoryObjectCollection as DirectoryObjectCollection,
)
from office365.intune.devices.alternative_security_id import (
    AlternativeSecurityId as AlternativeSecurityId,
)
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class Device(DirectoryObject):
    @property
    def alternative_security_ids(self): ...
    @property
    def device_id(self) -> str | None: ...
    @property
    def device_ownership(self) -> str | None: ...
    @property
    def member_of(self): ...
    @property
    def registered_owners(self): ...
    @property
    def registered_users(self): ...
    @property
    def transitive_member_of(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
