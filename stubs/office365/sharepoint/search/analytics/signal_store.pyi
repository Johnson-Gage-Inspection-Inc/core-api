from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.sharepoint.entity import Entity as Entity

class SignalStore(Entity):
    def __init__(self, context, resource_path) -> None: ...
    @property
    def entity_type_name(self): ...
