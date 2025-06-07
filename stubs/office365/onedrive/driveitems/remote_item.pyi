from _typeshed import Incomplete
from office365.directory.permissions.identity_set import IdentitySet as IdentitySet
from office365.onedrive.driveitems.image import Image as Image
from office365.onedrive.files.file import File as File
from office365.onedrive.files.system_info import FileSystemInfo as FileSystemInfo
from office365.onedrive.folders.folder import Folder as Folder
from office365.runtime.client_value import ClientValue as ClientValue

class RemoteItem(ClientValue):
    id: Incomplete
    createdBy: Incomplete
    createdDateTime: Incomplete
    file: Incomplete
    fileSystemInfo: Incomplete
    folder: Incomplete
    image: Incomplete
    def __init__(self, _id: Incomplete | None = None, created_by=..., created_datetime: Incomplete | None = None, file=..., file_system_info=..., folder=..., image=...) -> None: ...
