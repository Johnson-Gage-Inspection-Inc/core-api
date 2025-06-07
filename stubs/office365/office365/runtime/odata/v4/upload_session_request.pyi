import requests
import typing
from office365.runtime.client_request import ClientRequest as ClientRequest
from office365.runtime.http.http_method import HttpMethod as HttpMethod
from office365.runtime.http.request_options import RequestOptions as RequestOptions
from office365.runtime.queries.upload_session import (
    UploadSessionQuery as UploadSessionQuery,
)
from typing import Callable
from typing_extensions import Self

class UploadSessionRequest(ClientRequest):
    def __init__(
        self,
        file_object: typing.IO,
        chunk_size: int,
        chunk_uploaded: Callable[[int], None] = None,
    ) -> None: ...
    def build_request(self, query: UploadSessionQuery) -> Self: ...
    def process_response(
        self, response: requests.Response, query: UploadSessionQuery
    ) -> None: ...
    def execute_query(self, query: UploadSessionQuery) -> None: ...
    @property
    def file_size(self): ...
    @property
    def range_start(self): ...
    @property
    def range_end(self): ...
