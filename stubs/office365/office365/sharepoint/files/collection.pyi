from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.paths.service_operation import (
    ServiceOperationPath as ServiceOperationPath,
)
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.client_context import ClientContext as ClientContext
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection
from office365.sharepoint.files.creation_information import (
    FileCreationInformation as FileCreationInformation,
)
from office365.sharepoint.files.file import File as File
from office365.sharepoint.files.publish.status import FileStatus as FileStatus
from office365.sharepoint.folders.folder import Folder as Folder
from typing import IO

class FileCollection(EntityCollection[File]):
    def __init__(
        self,
        context: ClientContext,
        resource_path: ResourcePath = None,
        parent: Folder = None,
    ) -> None: ...
    def get_published_file(self, base_file_path): ...
    def upload(self, path_or_file: str | IO, file_name: str = None) -> File: ...
    def upload_with_checksum(self, file_object: IO, chunk_size: int = 1024) -> File: ...
    def create_upload_session(
        self,
        file,
        chunk_size,
        chunk_uploaded: Incomplete | None = None,
        file_name: Incomplete | None = None,
        **kwargs,
    ): ...
    def add(self, url, content, overwrite: bool = False): ...
    def add_template_file(self, url_of_file, template_file_type): ...
    def get_by_url(self, url: str) -> File: ...
    def get_by_id(self, _id: int) -> File: ...
    @property
    def parent(self) -> Folder: ...
