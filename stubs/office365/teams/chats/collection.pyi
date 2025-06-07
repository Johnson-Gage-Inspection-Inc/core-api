from _typeshed import Incomplete
from office365.entity_collection import EntityCollection as EntityCollection
from office365.teams.chats.chat import Chat as Chat

class ChatCollection(EntityCollection[Chat]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def add(self, chat_type): ...
