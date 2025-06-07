from _typeshed import Incomplete
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.teams.apps.app import TeamsApp as TeamsApp

class AppCatalogs(Entity):
    @property
    def teams_apps(self) -> EntityCollection[TeamsApp]: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
