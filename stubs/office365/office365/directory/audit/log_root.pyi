from _typeshed import Incomplete
from office365.directory.audit.directory import DirectoryAudit as DirectoryAudit
from office365.directory.audit.provisioning.object_summary import (
    ProvisioningObjectSummary as ProvisioningObjectSummary,
)
from office365.directory.audit.signins.signin import SignIn as SignIn
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class AuditLogRoot(Entity):
    @property
    def directory_audits(self) -> EntityCollection[DirectoryAudit]: ...
    @property
    def signins(self) -> EntityCollection[SignIn]: ...
    @property
    def provisioning(self) -> EntityCollection[ProvisioningObjectSummary]: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
