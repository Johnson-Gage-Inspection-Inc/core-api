from _typeshed import Incomplete
from office365.entity import Entity as Entity
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.teams.apps.app import TeamsApp as TeamsApp
from office365.teams.apps.definition import TeamsAppDefinition as TeamsAppDefinition

class TeamsAppInstallation(Entity):
    @property
    def teams_app(self): ...
    @property
    def teams_app_definition(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
