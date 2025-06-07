from office365.directory.insights.shared import SharedInsight as SharedInsight
from office365.directory.insights.trending import Trending as Trending
from office365.directory.insights.used import UsedInsight as UsedInsight
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class OfficeGraphInsights(Entity):
    @property
    def shared(self) -> EntityCollection[SharedInsight]: ...
    @property
    def trending(self) -> EntityCollection[Trending]: ...
    @property
    def used(self) -> EntityCollection[UsedInsight]: ...
