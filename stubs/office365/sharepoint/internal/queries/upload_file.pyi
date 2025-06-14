from typing import IO

from office365.runtime.http.http_method import HttpMethod as HttpMethod
from office365.runtime.http.request_options import RequestOptions as RequestOptions
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.attachments.attachment import Attachment as Attachment
from office365.sharepoint.files.file import File as File

def create_upload_file_query(
    file: File | Attachment, file_object: IO
) -> ServiceOperationQuery: ...
