from datetime import datetime

from _typeshed import Incomplete
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.teams.apps.installation import (
    TeamsAppInstallation as TeamsAppInstallation,
)
from office365.teams.chats.messages.info import ChatMessageInfo as ChatMessageInfo
from office365.teams.chats.messages.message import ChatMessage as ChatMessage
from office365.teams.chats.viewpoint import ChatViewpoint as ChatViewpoint
from office365.teams.members.conversation_collection import (
    ConversationMemberCollection as ConversationMemberCollection,
)
from office365.teams.operations.async_operation import (
    TeamsAsyncOperation as TeamsAsyncOperation,
)
from office365.teams.tabs.tab import TeamsTab as TeamsTab
from office365.teams.teamwork.online_meeting_info import (
    TeamworkOnlineMeetingInfo as TeamworkOnlineMeetingInfo,
)

class Chat(Entity):
    @property
    def chat_type(self) -> str | None: ...
    @property
    def created_datetime(self): ...
    @property
    def is_hidden_for_all_members(self) -> bool | None: ...
    @property
    def last_updated_datetime(self) -> datetime | None: ...
    @property
    def online_meeting_info(self) -> TeamworkOnlineMeetingInfo: ...
    @property
    def tenant_id(self) -> str | None: ...
    @property
    def topic(self) -> str | None: ...
    @property
    def viewpoint(self) -> ChatViewpoint: ...
    @property
    def web_url(self) -> str | None: ...
    @property
    def installed_apps(self) -> EntityCollection[TeamsAppInstallation]: ...
    @property
    def last_message_preview(self): ...
    @property
    def members(self) -> ConversationMemberCollection: ...
    @property
    def messages(self) -> EntityCollection[ChatMessage]: ...
    @property
    def operations(self) -> EntityCollection[TeamsAsyncOperation]: ...
    @property
    def tabs(self) -> EntityCollection[TeamsTab]: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
