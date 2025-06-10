from _typeshed import Incomplete
from office365.directory.security.alerts.alert import Alert as Alert
from office365.directory.security.alerts.comment import AlertComment as AlertComment
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class Incident(Entity):
    @property
    def assigned_to(self) -> str | None: ...
    @property
    def classification(self) -> str | None: ...
    @property
    def comments(self): ...
    @property
    def created_datetime(self): ...
    @property
    def alerts(self) -> EntityCollection[Alert]: ...
    @property
    def entity_type_name(self) -> str: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
