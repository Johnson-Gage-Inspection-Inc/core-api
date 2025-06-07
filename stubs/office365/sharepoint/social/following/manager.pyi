from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.social.actor import SocialActor as SocialActor

class SocialFollowingManager(Entity):
    def __init__(self, context) -> None: ...
    def get_followers(self): ...
    def get_suggestions(self): ...
