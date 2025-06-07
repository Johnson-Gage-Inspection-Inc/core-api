from _typeshed import Incomplete
from office365.onedrive.files.system_info import FileSystemInfo as FileSystemInfo
from office365.runtime.client_value import ClientValue as ClientValue

class DriveItemUploadableProperties(ClientValue):
    fileSystemInfo: Incomplete
    name: Incomplete
    description: Incomplete
    def __init__(
        self,
        file_system_info=...,
        name: Incomplete | None = None,
        description: Incomplete | None = None,
        file_size: Incomplete | None = None,
    ) -> None: ...
    @property
    def file_size(self): ...
