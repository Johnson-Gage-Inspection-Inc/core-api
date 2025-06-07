from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.sharepoint.activities.identity import ActivityIdentity as ActivityIdentity

class GetCommentFacet(ClientValue):
    assignees: Incomplete
    commentId: Incomplete
    isReply: Incomplete
    parentAuthor: Incomplete
    parentCommentId: Incomplete
    participants: Incomplete
    def __init__(self, assignees: Incomplete | None = None, comment_id: Incomplete | None = None, is_reply: Incomplete | None = None, parent_author=..., parent_comment_id: Incomplete | None = None, participants: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
