from _typeshed import Incomplete
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.publishing.video.channel_collection import (
    VideoChannelCollection as VideoChannelCollection,
)

class VideoServiceManager(Entity):
    def __init__(self, context) -> None: ...
    def get_channels(self, start_index: int = 0, limit: Incomplete | None = None): ...
