from _typeshed import Incomplete
from office365.directory.insights.resource_reference import ResourceReference as ResourceReference
from office365.directory.insights.usage_details import UsageDetails as UsageDetails
from office365.entity import Entity as Entity
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class UsedInsight(Entity):
    @property
    def last_used(self): ...
    @property
    def resource_reference(self): ...
    @property
    def resource(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
