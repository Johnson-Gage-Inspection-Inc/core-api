from _typeshed import Incomplete
from office365.directory.permissions.identity_set import IdentitySet as IdentitySet
from office365.entity_collection import EntityCollection as EntityCollection
from office365.onedrive.base_item import BaseItem as BaseItem
from office365.onedrive.driveitems.driveItem import DriveItem as DriveItem
from office365.onedrive.internal.paths.root import RootPath as RootPath
from office365.onedrive.listitems.list_item import ListItem as ListItem
from office365.onedrive.lists.list import List as List
from office365.onedrive.permissions.permission import Permission as Permission
from office365.onedrive.sites.site import Site as Site
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class SharedDriveItem(BaseItem):
    @property
    def items(self) -> EntityCollection[DriveItem]: ...
    @property
    def list_item(self) -> ListItem: ...
    @property
    def list(self) -> List: ...
    @property
    def drive_item(self) -> DriveItem: ...
    @property
    def owner(self): ...
    @property
    def root(self): ...
    @property
    def site(self): ...
    @property
    def permission(self): ...
    def get_property(self, name, default_value: Incomplete | None = None) -> None: ...
