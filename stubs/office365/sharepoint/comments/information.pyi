from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.sharepoint.comments.client.identity import Identity as Identity

class CommentInformation(ClientValue):
    text: Incomplete
    mentions: Incomplete
    def __init__(
        self, text: Incomplete | None = None, mentions: Incomplete | None = None
    ) -> None: ...
    @property
    def entity_type_name(self): ...
