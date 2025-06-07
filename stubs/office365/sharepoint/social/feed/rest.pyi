from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.social.feed.feed import SocialFeed as SocialFeed

class SocialRestFeed(Entity):
    def __init__(self, context) -> None: ...
    @property
    def social_feed(self): ...
