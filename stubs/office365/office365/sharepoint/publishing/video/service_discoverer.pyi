from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.sharepoint.entity import Entity as Entity

class VideoServiceDiscoverer(Entity):
    def __init__(self, context) -> None: ...
    @property
    def video_portal_url(self) -> str | None: ...
