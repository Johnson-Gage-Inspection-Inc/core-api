from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.intune.printing.services.endpoint import (
    PrintServiceEndpoint as PrintServiceEndpoint,
)
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class PrintService(Entity):
    def endpoints(self): ...
