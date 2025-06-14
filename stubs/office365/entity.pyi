from office365.graph_client import GraphClient as GraphClient
from office365.runtime.client_object import ClientObject as ClientObject
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.paths.v4.entity import EntityPath as EntityPath
from office365.runtime.queries.delete_entity import (
    DeleteEntityQuery as DeleteEntityQuery,
)
from office365.runtime.queries.update_entity import (
    UpdateEntityQuery as UpdateEntityQuery,
)
from typing import TypeVar
from typing_extensions import Self

T = TypeVar("T")

class Entity(ClientObject[T]):
    def update(self) -> Self: ...
    def delete_object(self) -> Self: ...
    @property
    def context(self) -> GraphClient: ...
    @property
    def entity_type_name(self) -> str: ...
    @property
    def id(self) -> str | None: ...
    @property
    def property_ref_name(self) -> str: ...
    def set_property(
        self, name: str, value: T, persist_changes: bool = True
    ) -> Self: ...
