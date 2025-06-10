from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.paths.service_operation import (
    ServiceOperationPath as ServiceOperationPath,
)
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.attachments.attachment import Attachment as Attachment
from office365.sharepoint.attachments.creation_information import (
    AttachmentCreationInformation as AttachmentCreationInformation,
)
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection
from typing import AnyStr, Callable, IO
from typing_extensions import Self

class AttachmentCollection(EntityCollection[Attachment]):
    def __init__(
        self,
        context,
        resource_path: Incomplete | None = None,
        parent: Incomplete | None = None,
    ) -> None: ...
    def add(
        self, attachment_file_information: AttachmentCreationInformation | dict
    ) -> Attachment: ...
    def add_using_path(
        self, decoded_url: str, content_stream: AnyStr
    ) -> Attachment: ...
    def delete_all(self): ...
    def download(
        self,
        download_file: IO,
        file_downloaded: Callable[[Attachment], None] | None = None,
    ) -> Self: ...
    def upload(self, file: IO, use_path: bool = True) -> Attachment: ...
    def get_by_filename(self, filename): ...
    def get_by_filename_as_path(self, decoded_url): ...
