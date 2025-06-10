from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.social.actor import SocialActor as SocialActor
from office365.sharepoint.social.attachment import SocialAttachment as SocialAttachment
from office365.sharepoint.social.feed.feed import SocialFeed as SocialFeed
from office365.sharepoint.social.thread import SocialThread as SocialThread

class SocialFeedManager(Entity):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def create_post(
        self,
        target_id: Incomplete | None = None,
        creation_data: Incomplete | None = None,
    ): ...
    def delete_post(self, post_id): ...
    def create_file_attachment(self, name, description, file_data): ...
    def get_feed(
        self, feed_type: Incomplete | None = None, options: Incomplete | None = None
    ): ...
    @property
    def owner(self): ...
    @property
    def personal_site_portal_uri(self): ...
