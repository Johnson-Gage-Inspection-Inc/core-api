from _typeshed import Incomplete
from office365.backuprestore.service_status import ServiceStatus as ServiceStatus
from office365.directory.protection.policy.one_drive_for_business import OneDriveForBusinessProtectionPolicy as OneDriveForBusinessProtectionPolicy
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class BackupRestoreRoot(Entity):
    @property
    def service_status(self): ...
    @property
    def one_drive_for_business_protection_policies(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
