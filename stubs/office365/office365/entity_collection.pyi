from typing import Any, TypeVar

from office365.entity import Entity as Entity
from office365.graph_client import GraphClient as GraphClient
from office365.runtime.client_object_collection import (
    ClientObjectCollection as ClientObjectCollection,
)
from office365.runtime.compat import is_string_type as is_string_type
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.paths.v4.entity import EntityPath as EntityPath
from office365.runtime.queries.create_entity import (
    CreateEntityQuery as CreateEntityQuery,
)
from typing_extensions import Self

T = TypeVar("T")

class EntityCollection(ClientObjectCollection[T]):
    def __init__(
        self,
        context: GraphClient,
        item_type: type[T],
        resource_path: ResourcePath | None = None,
        parent: Entity | None = None,
    ) -> None: ...
    def token(self, value): ...
    def __getitem__(self, key: int | str) -> T: ...
    def add(self, **kwargs: Any) -> T: ...
    def create_typed_object(
        self,
        initial_properties: dict | None = None,
        resource_path: ResourcePath | None = None,
    ) -> T: ...
    def set_property(
        self, key: str | int, value: dict, persist_changes: bool = False
    ) -> Self: ...
    @property
    def context(self) -> GraphClient: ...
