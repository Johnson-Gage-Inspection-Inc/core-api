from office365.delta_path import DeltaPath as DeltaPath
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.graph_client import GraphClient as GraphClient
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from typing import TypeVar

T = TypeVar('T')

class DeltaCollection(EntityCollection[T]):
    def __init__(self, context: GraphClient, item_type: type[T], resource_path: ResourcePath | None = None, parent: Entity | None = None) -> None: ...
    def change_type(self, type_name): ...
    @property
    def delta(self) -> DeltaCollection[T]: ...
