from _typeshed import Incomplete
from office365.directory.protection.risk_detection import RiskDetection as RiskDetection
from office365.directory.protection.riskyusers.collection import (
    RiskyUserCollection as RiskyUserCollection,
)
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class IdentityProtectionRoot(Entity):
    @property
    def risk_detections(self): ...
    @property
    def risky_users(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
