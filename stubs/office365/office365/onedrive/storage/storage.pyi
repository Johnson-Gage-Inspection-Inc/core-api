from office365.entity import Entity as Entity
from office365.onedrive.filestorage.file_storage import FileStorage as FileStorage
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class Storage(Entity):
    @property
    def file_storage(self): ...
