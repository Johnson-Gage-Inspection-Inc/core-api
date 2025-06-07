from _typeshed import Incomplete
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.onedrive.driveitems.driveItem import DriveItem as DriveItem
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.compat import quote as quote
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.function import FunctionQuery as FunctionQuery
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.teams.channels.provision_email_result import (
    ProvisionChannelEmailResult as ProvisionChannelEmailResult,
)
from office365.teams.chats.messages.message import ChatMessage as ChatMessage
from office365.teams.members.conversation import (
    ConversationMember as ConversationMember,
)
from office365.teams.tabs.tab import TeamsTab as TeamsTab

class Channel(Entity):
    def does_user_have_access(
        self,
        user_id: str = None,
        tenant_id: str = None,
        user_principal_name: str = None,
    ) -> ClientResult[bool]: ...
    def provision_email(self): ...
    def remove_email(self): ...
    @property
    def files_folder(self): ...
    @property
    def tabs(self) -> EntityCollection[TeamsTab]: ...
    @property
    def messages(self) -> EntityCollection[ChatMessage]: ...
    @property
    def members(self) -> EntityCollection[ConversationMember]: ...
    @property
    def membership_type(self) -> str | None: ...
    @property
    def web_url(self) -> str | None: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
    def set_property(self, name, value, persist_changes: bool = True): ...
