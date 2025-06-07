from office365.entity_collection import EntityCollection as EntityCollection
from office365.onedrive.base_item import BaseItem as BaseItem
from office365.onedrive.recyclebin.item import RecycleBinItem as RecycleBinItem
from office365.onedrive.recyclebin.settings import RecycleBinSettings as RecycleBinSettings
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class RecycleBin(BaseItem):
    @property
    def items(self) -> EntityCollection[RecycleBinItem]: ...
    @property
    def settings(self): ...
