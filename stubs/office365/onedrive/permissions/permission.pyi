from _typeshed import Incomplete
from office365.directory.permissions.identity_set import IdentitySet as IdentitySet
from office365.entity import Entity as Entity
from office365.onedrive.drives.recipient import DriveRecipient as DriveRecipient
from office365.onedrive.listitems.item_reference import ItemReference as ItemReference
from office365.onedrive.permissions.sharepoint_identity_set import (
    SharePointIdentitySet as SharePointIdentitySet,
)
from office365.onedrive.permissions.sharing_invitation import (
    SharingInvitation as SharingInvitation,
)
from office365.onedrive.permissions.sharing_link import SharingLink as SharingLink
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.runtime.types.collections import StringCollection as StringCollection

class Permission(Entity):
    def grant(self, recipients, roles): ...
    @property
    def invitation(self): ...
    @property
    def granted_to(self): ...
    @property
    def granted_to_v2(self): ...
    @property
    def granted_to_identities(self): ...
    @property
    def granted_to_identities_v2(self): ...
    @property
    def link(self) -> SharingLink: ...
    @property
    def roles(self): ...
    @roles.setter
    def roles(self, value) -> None: ...
    @property
    def share_id(self) -> str | None: ...
    @property
    def has_password(self) -> bool | None: ...
    @property
    def inherited_from(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
