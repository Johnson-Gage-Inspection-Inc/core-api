from _typeshed import Incomplete
from office365.runtime.paths.service_operation import (
    ServiceOperationPath as ServiceOperationPath,
)
from office365.runtime.paths.v3.entity import EntityPath as EntityPath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection
from office365.sharepoint.folders.coloring_information import (
    FolderColoringInformation as FolderColoringInformation,
)
from office365.sharepoint.folders.folder import Folder as Folder

class FolderCollection(EntityCollection[Folder]):
    def __init__(
        self,
        context,
        resource_path: Incomplete | None = None,
        parent: Incomplete | None = None,
    ) -> None: ...
    def add_using_path(self, decoded_url, overwrite): ...
    def ensure_path(self, path): ...
    def add(self, name, color_hex: Incomplete | None = None): ...
    def get_by_url(self, url): ...
    def get_by_path(self, decoded_url): ...
