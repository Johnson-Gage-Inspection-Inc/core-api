from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.sharepoint.entity import Entity as Entity

class Alert(Entity):
    @property
    def alert_frequency(self) -> int | None: ...
    @property
    def alert_template_name(self) -> int | None: ...
    @property
    def always_notify(self) -> bool | None: ...
    @property
    def item(self): ...
    @property
    def user(self): ...
    @property
    def list(self): ...
