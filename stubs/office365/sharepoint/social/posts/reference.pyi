from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.sharepoint.social.posts.post import SocialPost as SocialPost

class SocialPostReference(ClientValue):
    Digest: Incomplete
    Post: Incomplete
    ThreadId: Incomplete
    ThreadOwnerIndex: Incomplete
    def __init__(self, digest: Incomplete | None = None, post=..., thread_id: Incomplete | None = None, thread_owner_index: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
