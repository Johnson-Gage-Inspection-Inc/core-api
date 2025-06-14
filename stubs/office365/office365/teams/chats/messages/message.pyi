from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.outlook.mail.item_body import ItemBody as ItemBody
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.teams.channels.iIdentity import ChannelIdentity as ChannelIdentity
from office365.teams.chats.messages.attachment import (
    ChatMessageAttachment as ChatMessageAttachment,
)

class ChatMessage(Entity):
    @property
    def attachments(self): ...
    @property
    def body(self): ...
    @property
    def channel_identity(self): ...
    @property
    def replies(self): ...
    @property
    def subject(self) -> str | None: ...
    @property
    def summary(self) -> str | None: ...
    @property
    def web_url(self) -> str | None: ...
    @property
    def importance(self) -> str | None: ...
