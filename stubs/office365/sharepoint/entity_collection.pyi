from office365.runtime.client_object_collection import ClientObjectCollection as ClientObjectCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.paths.v3.entity import EntityPath as EntityPath
from office365.sharepoint.client_context import ClientContext as ClientContext
from office365.sharepoint.entity import Entity as Entity
from typing import TypeVar

T = TypeVar('T')

class EntityCollection(ClientObjectCollection[T]):
    def __init__(self, context: ClientContext, item_type: type[T], resource_path: ResourcePath | None = None, parent: Entity | None = None) -> None: ...
    def create_typed_object(self, initial_properties: dict | None = None, resource_path: ResourcePath | None = None) -> T: ...
    @property
    def context(self) -> ClientContext: ...
