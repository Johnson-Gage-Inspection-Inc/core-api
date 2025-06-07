from office365.entity import Entity as Entity
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class TeamInfo(Entity):
    @property
    def display_name(self) -> str | None: ...
    @property
    def team(self): ...
