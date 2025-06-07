from _typeshed import Incomplete
from office365.runtime.client_request_exception import (
    ClientRequestException as ClientRequestException,
)
from office365.runtime.client_runtime_context import (
    ClientRuntimeContext as ClientRuntimeContext,
)
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.http.request_options import RequestOptions as RequestOptions
from typing import Callable, Generic, TypeVar
from typing_extensions import Self

T = TypeVar("T")

class ClientResult(Generic[T]):
    def __init__(
        self, context: ClientRuntimeContext, default_value: T | None = None
    ) -> None: ...
    def before_execute(self, action: Callable[[RequestOptions], None]) -> Self: ...
    def after_execute(
        self,
        action: Callable[[Self], None],
        execute_first: bool = False,
        include_response: bool = False,
    ) -> Self: ...
    def set_property(
        self, key: str, value: T, persist_changes: bool = False
    ) -> Self: ...
    @property
    def value(self): ...
    def execute_query(self): ...
    def execute_query_retry(
        self,
        max_retry: int = 5,
        timeout_secs: int = 5,
        success_callback: Incomplete | None = None,
        failure_callback: Incomplete | None = None,
        exceptions=...,
    ): ...
