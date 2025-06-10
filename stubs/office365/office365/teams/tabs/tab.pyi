from _typeshed import Incomplete
from office365.entity import Entity as Entity
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.teams.apps.app import TeamsApp as TeamsApp
from office365.teams.tabs.configuration import (
    TeamsTabConfiguration as TeamsTabConfiguration,
)

class TeamsTab(Entity):
    @property
    def teams_app(self): ...
    @property
    def configuration(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
