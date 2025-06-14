from office365.runtime.client_result import ClientResult as ClientResult
from office365.sharepoint.directory.my_groups_result import (
    MyGroupsResult as MyGroupsResult,
)
from office365.sharepoint.entity import Entity as Entity

class User(Entity):
    @property
    def about_me(self) -> str | None: ...
    @property
    def account_enabled(self) -> bool | None: ...
    def is_member_of(self, group_id: str) -> ClientResult[bool]: ...
    def get_my_groups(self): ...
    @property
    def entity_type_name(self): ...
