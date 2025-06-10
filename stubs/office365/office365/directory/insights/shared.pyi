from _typeshed import Incomplete
from office365.directory.insights.resource_reference import (
    ResourceReference as ResourceReference,
)
from office365.directory.insights.sharing_detail import SharingDetail as SharingDetail
from office365.entity import Entity as Entity
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class SharedInsight(Entity):
    @property
    def last_shared(self): ...
    @property
    def resource_reference(self) -> ResourceReference: ...
    @property
    def resource(self) -> Entity: ...
    @property
    def sharing_history(self) -> ClientValueCollection[SharingDetail]: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
