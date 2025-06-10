from _typeshed import Incomplete
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.sharing.abilities import SharingAbilities as SharingAbilities
from office365.sharepoint.sharing.access_request_settings import (
    AccessRequestSettings as AccessRequestSettings,
)
from office365.sharepoint.sharing.domain_restriction_settings import (
    DomainRestrictionSettings as DomainRestrictionSettings,
)
from office365.sharepoint.sharing.links.default_templates_collection import (
    SharingLinkDefaultTemplatesCollection as SharingLinkDefaultTemplatesCollection,
)
from office365.sharepoint.sharing.permission_collection import (
    PermissionCollection as PermissionCollection,
)
from office365.sharepoint.sharing.picker_settings import (
    PickerSettings as PickerSettings,
)

class SharingInformation(Entity):
    @property
    def access_request_settings(self): ...
    @property
    def anonymous_link_expiration_restriction_days(self) -> int | None: ...
    @property
    def domain_restriction_settings(self): ...
    @property
    def permissions_information(self): ...
    @property
    def picker_settings(self): ...
    @property
    def sharing_abilities(self): ...
    @property
    def sharing_link_templates(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
    @property
    def entity_type_name(self): ...
