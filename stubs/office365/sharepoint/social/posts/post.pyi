from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.sharepoint.social.attachment import SocialAttachment as SocialAttachment
from office365.sharepoint.social.data_overlay import SocialDataOverlay as SocialDataOverlay
from office365.sharepoint.social.link import SocialLink as SocialLink
from office365.sharepoint.social.posts.actor_info import SocialPostActorInfo as SocialPostActorInfo

class SocialPost(ClientValue):
    Attachment: Incomplete
    Overlays: Incomplete
    Source: Incomplete
    LikerInfo: Incomplete
    def __init__(self, attachment=..., overlays: Incomplete | None = None, source=..., liker_info=...) -> None: ...
