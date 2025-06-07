from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class RiskyUser(Entity):
    @property
    def history(self): ...
    @property
    def user_principal_name(self) -> str | None: ...
