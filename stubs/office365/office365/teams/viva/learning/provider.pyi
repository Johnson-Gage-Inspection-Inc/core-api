from _typeshed import Incomplete
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.teams.viva.learning.content import LearningContent as LearningContent

class LearningProvider(Entity):
    @property
    def learning_contents(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
