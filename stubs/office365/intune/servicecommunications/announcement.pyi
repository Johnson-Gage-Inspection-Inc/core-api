from _typeshed import Incomplete
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.intune.servicecommunications.health.health import ServiceHealth as ServiceHealth
from office365.intune.servicecommunications.issues.issue import ServiceHealthIssue as ServiceHealthIssue
from office365.intune.servicecommunications.messages.update import ServiceUpdateMessage as ServiceUpdateMessage
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class ServiceAnnouncement(Entity):
    @property
    def health_overviews(self): ...
    @property
    def issues(self): ...
    @property
    def messages(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
