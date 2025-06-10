from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.search.external.connection import (
    ExternalConnection as ExternalConnection,
)

class External(Entity):
    @property
    def connections(self) -> EntityCollection[ExternalConnection]: ...
