from office365.admin.sharepoint_settings import SharepointSettings as SharepointSettings
from office365.entity import Entity as Entity
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class Sharepoint(Entity):
    @property
    def settings(self) -> SharepointSettings: ...
