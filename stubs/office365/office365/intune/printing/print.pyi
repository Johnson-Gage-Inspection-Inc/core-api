from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.intune.printing.connectors.connector import (
    PrintConnector as PrintConnector,
)
from office365.intune.printing.share import PrinterShare as PrinterShare
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class Print(Entity):
    @property
    def connectors(self): ...
    @property
    def shares(self): ...
