from office365.entity import Entity as Entity
from office365.intune.audit.actor import AuditActor as AuditActor
from office365.intune.audit.resource import AuditResource as AuditResource
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)

class AuditEvent(Entity):
    @property
    def activity(self) -> str | None: ...
    @property
    def actor(self): ...
    @property
    def resources(self): ...
