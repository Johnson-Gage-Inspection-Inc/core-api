from office365.runtime.types.collections import StringCollection as StringCollection
from office365.teams.schedule.change_tracked_entity import ChangeTrackedEntity as ChangeTrackedEntity

class SchedulingGroup(ChangeTrackedEntity):
    @property
    def is_active(self) -> bool | None: ...
    @property
    def user_ids(self): ...
