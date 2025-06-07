from _typeshed import Incomplete
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.teams.members.conversation import ConversationMember as ConversationMember

class AadUserConversationMember(ConversationMember):
    @property
    def user_id(self) -> str | None: ...
    @property
    def user(self): ...
    def to_json(self, json_format: Incomplete | None = None): ...
