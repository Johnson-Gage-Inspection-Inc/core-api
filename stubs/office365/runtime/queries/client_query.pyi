from typing import AnyStr, Generic, TypeVar

from office365.runtime.client_object import ClientObject as ClientObject
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.client_runtime_context import (
    ClientRuntimeContext as ClientRuntimeContext,
)
from office365.runtime.client_value import ClientValue as ClientValue

T = TypeVar("T", bound="ClientObject" | "ClientResult")

class ClientQuery(Generic[T]):
    def __init__(
        self,
        context: ClientRuntimeContext,
        binding_type: ClientObject | None = None,
        parameters_type: ClientObject | ClientValue | dict | AnyStr | None = None,
        parameters_name: str | None = None,
        return_type: T | None = None,
    ) -> None: ...
    def build_request(self): ...
    def execute_query(self): ...
    @property
    def url(self): ...
    @property
    def query_options(self): ...
    @property
    def path(self): ...
    @property
    def context(self): ...
    @property
    def id(self): ...
    @property
    def binding_type(self): ...
    @property
    def parameters_name(self): ...
    @property
    def parameters_type(self): ...
    @property
    def return_type(self): ...
