from office365.communications.callrecords.endpoint import Endpoint as Endpoint
from office365.entity import Entity as Entity

class Segment(Entity):
    @property
    def callee(self): ...
    @property
    def caller(self): ...
    @property
    def entity_type_name(self): ...
