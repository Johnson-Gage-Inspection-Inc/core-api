from _typeshed import Incomplete
from office365.runtime.compat import get_mime_type as get_mime_type
from office365.runtime.compat import (
    message_as_bytes_or_string as message_as_bytes_or_string,
)
from office365.runtime.http.http_method import HttpMethod as HttpMethod
from office365.runtime.http.request_options import RequestOptions as RequestOptions
from office365.runtime.queries.batch import create_boundary as create_boundary
from office365.runtime.queries.client_query import ClientQuery as ClientQuery

class OneNotePageCreateQuery(ClientQuery):
    def __init__(
        self, pages, presentation_file, attachment_files: Incomplete | None = None
    ) -> None: ...
    @property
    def return_type(self): ...
