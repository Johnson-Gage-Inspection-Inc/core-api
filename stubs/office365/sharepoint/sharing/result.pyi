from _typeshed import Incomplete
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.principal.groups.collection import (
    GroupCollection as GroupCollection,
)
from office365.sharepoint.principal.groups.group import Group as Group
from office365.sharepoint.principal.users.collection import (
    UserCollection as UserCollection,
)
from office365.sharepoint.sharing.invitation.creation_result import (
    SPInvitationCreationResult as SPInvitationCreationResult,
)
from office365.sharepoint.sharing.user_sharing_result import (
    UserSharingResult as UserSharingResult,
)

class SharingResult(Entity):
    @property
    def url(self) -> str | None: ...
    @property
    def error_message(self) -> str | None: ...
    @property
    def name(self) -> str | None: ...
    @property
    def icon_url(self) -> str | None: ...
    @property
    def status_code(self) -> int | None: ...
    @property
    def permissions_page_relative_url(self) -> str | None: ...
    @property
    def invited_users(self) -> ClientValueCollection[SPInvitationCreationResult]: ...
    @property
    def uniquely_permissioned_users(
        self,
    ) -> ClientValueCollection[UserSharingResult]: ...
    @property
    def groups_shared_with(self): ...
    @property
    def group_users_added_to(self): ...
    @property
    def users_with_access_requests(self): ...
    @property
    def users_added_to_group(self) -> ClientValueCollection[UserSharingResult]: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
    def set_property(self, name, value, persist_changes: bool = True): ...
