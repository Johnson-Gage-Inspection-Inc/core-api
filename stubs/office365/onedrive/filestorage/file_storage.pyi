from office365.entity import Entity as Entity
from office365.onedrive.filestorage.container_collection import FileStorageContainerCollection as FileStorageContainerCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class FileStorage(Entity):
    @property
    def containers(self): ...
