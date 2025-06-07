from office365.runtime.odata.json_format import ODataJsonFormat as ODataJsonFormat
from office365.runtime.odata.v3.json_light_format import (
    JsonLightFormat as JsonLightFormat,
)
from typing import Any, Iterator, TypeVar
from typing_extensions import Self

P_T = TypeVar("P_T", int, float, str, bool, "ClientValue")

class ClientValue:
    def set_property(
        self, k: str | int, v: Any, persist_changes: bool = True
    ) -> Self: ...
    def get_property(self, k: str) -> P_T: ...
    def __iter__(self) -> Iterator[tuple[str, P_T]]: ...
    def to_json(self, json_format: ODataJsonFormat | None = None) -> dict: ...
    @property
    def entity_type_name(self) -> str: ...
