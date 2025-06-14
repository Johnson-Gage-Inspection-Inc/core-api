from _typeshed import Incomplete
from office365.runtime.client_object_collection import (
    ClientObjectCollection as ClientObjectCollection,
)
from office365.runtime.client_request_exception import (
    ClientRequestException as ClientRequestException,
)
from office365.runtime.client_runtime_context import (
    ClientRuntimeContext as ClientRuntimeContext,
)
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.http.request_options import RequestOptions as RequestOptions
from office365.runtime.odata.json_format import ODataJsonFormat as ODataJsonFormat
from office365.runtime.odata.query_options import QueryOptions as QueryOptions
from office365.runtime.odata.type import ODataType as ODataType
from office365.runtime.odata.v3.json_light_format import (
    JsonLightFormat as JsonLightFormat,
)
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from requests import Response
from typing import Any, Callable, Generic, TypeVar
from typing_extensions import Self

T = TypeVar("T")
P_T = TypeVar("P_T")

class ClientObject(Generic[T]):
    def __init__(
        self,
        context: ClientRuntimeContext,
        resource_path: ResourcePath | None = None,
        parent_collection: ClientObjectCollection | None = None,
    ) -> None: ...
    def clear_state(self) -> Self: ...
    def execute_query(self) -> Self: ...
    def execute_query_retry(
        self,
        max_retry: int = 5,
        timeout_secs: int = 5,
        success_callback: Incomplete | None = None,
        failure_callback: Incomplete | None = None,
        exceptions=...,
    ): ...
    def before_execute(self, action: Callable[[RequestOptions], None]) -> Self: ...
    def after_execute(
        self,
        action: Callable[[Self | Response], None],
        execute_first: bool = False,
        include_response: bool = False,
    ) -> Self: ...
    def get(self) -> Self: ...
    def is_property_available(self, name: str) -> bool: ...
    def expand(self, names: list[str]) -> Self: ...
    def select(self, names: list[str]) -> Self: ...
    def remove_from_parent_collection(self): ...
    def get_property(self, name: str, default_value: P_T = None) -> P_T: ...
    def set_property(
        self, name: str | int, value: P_T, persist_changes: bool = True
    ) -> Self: ...
    def ensure_property(
        self,
        name: str,
        action: Callable[..., None],
        *args: Any | None,
        **kwargs: Any | None,
    ) -> Self: ...
    def ensure_properties(
        self, names: list[str], action: Callable[..., None], *args: Any, **kwargs: Any
    ) -> Self: ...
    @property
    def entity_type_name(self): ...
    @property
    def property_ref_name(self) -> str | None: ...
    @property
    def resource_url(self) -> str | None: ...
    @property
    def context(self): ...
    @property
    def resource_path(self): ...
    @property
    def query_options(self): ...
    @property
    def properties(self): ...
    @property
    def persistable_properties(self): ...
    @property
    def parent_collection(self): ...
    def to_json(self, json_format: ODataJsonFormat | None = None) -> dict: ...
