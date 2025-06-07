from _typeshed import Incomplete
from office365.directory.invitations.message_info import (
    InvitedUserMessageInfo as InvitedUserMessageInfo,
)
from office365.directory.users.user import User as User
from office365.entity import Entity as Entity
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class Invitation(Entity):
    @property
    def invited_user_display_name(self) -> str | None: ...
    @property
    def invited_user_email_address(self) -> str | None: ...
    @property
    def invited_user_message_info(self): ...
    @property
    def invited_user(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
