from _typeshed import Incomplete
from office365.directory.permissions.identity_set import IdentitySet as IdentitySet
from office365.entity import Entity as Entity

class ThreatAssessmentRequest(Entity):
    @property
    def created_by(self): ...
    @property
    def created_datetime(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
