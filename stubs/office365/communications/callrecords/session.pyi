from office365.communications.callrecords.segment import Segment as Segment
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class Session(Entity):
    @property
    def segments(self): ...
