from _typeshed import Incomplete
from office365.directory.permissions.identity_set import IdentitySet as IdentitySet
from office365.entity import Entity as Entity
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class ItemActivity(Entity):
    @property
    def actor(self): ...
    @property
    def drive_item(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
