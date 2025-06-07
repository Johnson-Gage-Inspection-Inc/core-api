from _typeshed import Incomplete
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.queries.function import FunctionQuery as FunctionQuery
from office365.teams.channels.channel import Channel as Channel
from office365.teams.chats.messages.message import ChatMessage as ChatMessage

class ChannelCollection(EntityCollection[Channel]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def add(self, display_name, description: Incomplete | None = None, membership_type: Incomplete | None = None, **kwargs): ...
    def get_all_messages(self): ...
