from _typeshed import Incomplete
from office365.entity_collection import EntityCollection as EntityCollection
from office365.teams.members.conversation import (
    ConversationMember as ConversationMember,
)

class ConversationMemberCollection(EntityCollection[ConversationMember]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def add(
        self, user, roles, visible_history_start_datetime: Incomplete | None = None
    ): ...
