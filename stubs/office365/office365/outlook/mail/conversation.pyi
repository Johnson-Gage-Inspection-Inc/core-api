import datetime

from _typeshed import Incomplete
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.outlook.mail.conversation_thread import (
    ConversationThread as ConversationThread,
)
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.types.collections import StringCollection as StringCollection

class Conversation(Entity):
    @property
    def has_attachments(self) -> bool | None: ...
    @property
    def last_delivered_datetime(self) -> datetime.datetime | None: ...
    @property
    def preview(self) -> str | None: ...
    @property
    def topic(self) -> str | None: ...
    @property
    def unique_senders(self): ...
    @property
    def threads(self) -> EntityCollection[ConversationThread]: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
