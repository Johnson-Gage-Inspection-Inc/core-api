from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.teams.deleted import DeletedTeam as DeletedTeam

class Teamwork(Entity):
    @property
    def is_teams_enabled(self) -> bool | None: ...
    @property
    def region(self) -> str | None: ...
    @property
    def deleted_teams(self): ...
