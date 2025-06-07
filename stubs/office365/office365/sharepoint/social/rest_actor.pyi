from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.social.actor import SocialActor as SocialActor

class SocialRestActor(Entity):
    @property
    def me(self): ...
    @property
    def entity_type_name(self): ...
