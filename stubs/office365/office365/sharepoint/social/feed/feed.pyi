from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.sharepoint.social.thread import SocialThread as SocialThread

class SocialFeed(ClientValue):
    Attributes: Incomplete
    NewestProcessed: Incomplete
    OldestProcessed: Incomplete
    Threads: Incomplete
    UnreadMentionCount: Incomplete
    def __init__(
        self,
        attributes: Incomplete | None = None,
        newest_processed: Incomplete | None = None,
        oldest_processed: Incomplete | None = None,
        threads: Incomplete | None = None,
        unread_mention_count: Incomplete | None = None,
    ) -> None: ...
    @property
    def entity_type_name(self): ...
