from _typeshed import Incomplete
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection
from office365.sharepoint.publishing.video.item import VideoItem as VideoItem

class VideoItemCollection(EntityCollection):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
