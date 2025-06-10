from office365.directory.users.activities.activity import UserActivity as UserActivity
from office365.entity import Entity as Entity
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class ActivityHistoryItem(Entity):
    @property
    def active_duration_seconds(self) -> int | None: ...
    @property
    def created_datetime(self): ...
    @property
    def activity(self): ...
