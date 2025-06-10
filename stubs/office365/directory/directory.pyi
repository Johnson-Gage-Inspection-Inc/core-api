from _typeshed import Incomplete
from office365.directory.administrative_unit import (
    AdministrativeUnit as AdministrativeUnit,
)
from office365.directory.custom_security_attribute_definition import (
    CustomSecurityAttributeDefinition as CustomSecurityAttributeDefinition,
)
from office365.directory.device_local_credential_info import (
    DeviceLocalCredentialInfo as DeviceLocalCredentialInfo,
)
from office365.directory.object_collection import (
    DirectoryObjectCollection as DirectoryObjectCollection,
)
from office365.directory.subscriptions.company import (
    CompanySubscription as CompanySubscription,
)
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class Directory(Entity):
    @property
    def device_local_credentials(self): ...
    @property
    def administrative_units(self): ...
    @property
    def custom_security_attribute_definitions(self): ...
    @property
    def subscriptions(self): ...
    def deleted_items(self, entity_type: Incomplete | None = None): ...
    @property
    def deleted_groups(self): ...
    @property
    def deleted_users(self): ...
    @property
    def deleted_applications(self): ...
    @property
    def deleted_service_principals(self): ...
