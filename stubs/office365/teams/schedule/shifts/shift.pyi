from _typeshed import Incomplete
from office365.teams.schedule.change_tracked_entity import ChangeTrackedEntity as ChangeTrackedEntity
from office365.teams.schedule.shifts.item import ShiftItem as ShiftItem

class Shift(ChangeTrackedEntity):
    @property
    def draft_shift(self): ...
    @property
    def shared_shift(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
