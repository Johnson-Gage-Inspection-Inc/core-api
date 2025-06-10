from _typeshed import Incomplete
from office365.entity_collection import EntityCollection as EntityCollection
from office365.outlook.mail.attachments.attachment import Attachment as Attachment
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.compat import parse_query_string as parse_query_string
from office365.runtime.http.request_options import RequestOptions as RequestOptions
from office365.runtime.odata.v4.upload_session import UploadSession as UploadSession
from office365.runtime.odata.v4.upload_session_request import (
    UploadSessionRequest as UploadSessionRequest,
)
from office365.runtime.queries.upload_session import (
    UploadSessionQuery as UploadSessionQuery,
)

class AttachmentCollection(EntityCollection[Attachment]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def add_file(
        self,
        name,
        content: Incomplete | None = None,
        content_type: Incomplete | None = None,
        base64_content: Incomplete | None = None,
    ): ...
    def resumable_upload(
        self,
        source_path,
        chunk_size: int = 1000000,
        chunk_uploaded: Incomplete | None = None,
    ): ...
    def create_upload_session(self, attachment_item): ...
