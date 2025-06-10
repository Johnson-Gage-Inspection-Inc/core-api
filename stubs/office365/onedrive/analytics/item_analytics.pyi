from _typeshed import Incomplete
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.onedrive.analytics.item_activity_stat import (
    ItemActivityStat as ItemActivityStat,
)
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class ItemAnalytics(Entity):
    @property
    def all_time(self): ...
    @property
    def item_activity_stats(self) -> EntityCollection[ItemActivityStat]: ...
    @property
    def last_seven_days(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
