from _typeshed import Incomplete
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.teams.apps.definition import TeamsAppDefinition as TeamsAppDefinition

class TeamsApp(Entity):
    @property
    def display_name(self) -> str | None: ...
    @property
    def distribution_method(self) -> str | None: ...
    @property
    def app_definitions(self) -> EntityCollection[TeamsAppDefinition]: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
