from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.sharepoint.social.actor import SocialActor as SocialActor
from office365.sharepoint.social.posts.post import SocialPost as SocialPost
from office365.sharepoint.social.posts.reference import SocialPostReference as SocialPostReference

class SocialThread(ClientValue):
    Id: Incomplete
    Actors: Incomplete
    RootPost: Incomplete
    Replies: Incomplete
    PostReference: Incomplete
    def __init__(self, thread_id: Incomplete | None = None, actors: Incomplete | None = None, replies: Incomplete | None = None, root_post=..., post_reference=...) -> None: ...
    @property
    def entity_type_name(self): ...
