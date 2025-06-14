from datetime import datetime

from _typeshed import Incomplete
from office365.directory.insights.resource_reference import (
    ResourceReference as ResourceReference,
)
from office365.entity import Entity as Entity
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class Trending(Entity):
    @property
    def last_modified_datetime(self) -> datetime | None: ...
    @property
    def resource_reference(self) -> ResourceReference: ...
    @property
    def resource(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
