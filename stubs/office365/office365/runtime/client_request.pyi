import abc
import requests
from _typeshed import Incomplete
from abc import abstractmethod
from office365.runtime.client_request_exception import (
    ClientRequestException as ClientRequestException,
)
from office365.runtime.http.http_method import HttpMethod as HttpMethod
from office365.runtime.http.request_options import RequestOptions as RequestOptions
from office365.runtime.queries.client_query import ClientQuery as ClientQuery
from office365.runtime.types.event_handler import EventHandler as EventHandler

class ClientRequest(metaclass=abc.ABCMeta):
    beforeExecute: Incomplete
    afterExecute: Incomplete
    def __init__(self) -> None: ...
    @abstractmethod
    def build_request(self, query: ClientQuery) -> RequestOptions: ...
    @abstractmethod
    def process_response(
        self, response: requests.Response, query: ClientQuery
    ) -> None: ...
    def execute_query(self, query: ClientQuery) -> None: ...
    def execute_request_direct(self, request: RequestOptions) -> requests.Response: ...
