from office365.runtime.compat import (
    is_absolute_url as is_absolute_url,
    urlparse as urlparse,
)
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class WebPath(ResourcePath):
    @property
    def segment(self): ...
    @property
    def web_path(self): ...
    @property
    def parent(self) -> None: ...
