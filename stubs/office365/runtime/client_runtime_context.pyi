import abc
from _typeshed import Incomplete
from office365.runtime.client_object import T as T
from office365.runtime.client_request import ClientRequest as ClientRequest
from office365.runtime.client_request_exception import (
    ClientRequestException as ClientRequestException,
)
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.http.http_method import HttpMethod as HttpMethod
from office365.runtime.http.request_options import RequestOptions as RequestOptions
from office365.runtime.queries.client_query import ClientQuery as ClientQuery
from office365.runtime.queries.read_entity import ReadEntityQuery as ReadEntityQuery
from requests import Response
from typing import AnyStr, Callable
from typing_extensions import Self

class ClientRuntimeContext(metaclass=abc.ABCMeta):
    def __init__(self) -> None: ...
    @property
    def current_query(self) -> ClientQuery: ...
    @property
    def has_pending_request(self): ...
    def build_request(self, query: ClientQuery) -> RequestOptions: ...
    def execute_query_retry(
        self,
        max_retry: int = 5,
        timeout_secs: int = 5,
        success_callback: Incomplete | None = None,
        failure_callback: Incomplete | None = None,
        exceptions=...,
    ) -> None: ...
    @abc.abstractmethod
    def pending_request(self) -> ClientRequest: ...
    @abc.abstractmethod
    def service_root_url(self) -> str: ...
    def load(
        self, client_object: T, properties_to_retrieve: list[str] = None
    ) -> Self: ...
    def before_query_execute(
        self, action: Callable[[RequestOptions], None], once: bool = True
    ) -> Self: ...
    def before_execute(
        self, action: Callable[[RequestOptions], None], once: bool = True
    ) -> Self: ...
    def after_query_execute(
        self,
        action: Callable[[T | Response], None],
        execute_first: bool = False,
        include_response: bool = False,
    ) -> Self: ...
    def after_execute(
        self, action: Callable[[Response], None], once: bool = True
    ) -> Self: ...
    def execute_request_direct(self, path: str) -> Response: ...
    def execute_query(self): ...
    def add_query(self, query: ClientQuery) -> Self: ...
    def clear(self): ...
    def get_metadata(self) -> ClientResult[AnyStr]: ...
