from office365.runtime.compat import is_absolute_url as is_absolute_url
from office365.runtime.compat import urlparse as urlparse
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.paths.v4.entity import EntityPath as EntityPath

class SitePath(EntityPath):
    @property
    def segment(self): ...
    @property
    def collection(self): ...
