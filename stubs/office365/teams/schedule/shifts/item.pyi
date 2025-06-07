from _typeshed import Incomplete
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.teams.schedule.entity import ScheduleEntity as ScheduleEntity
from office365.teams.schedule.shifts.activity import ShiftActivity as ShiftActivity

class ShiftItem(ScheduleEntity):
    displayName: Incomplete
    activities: Incomplete
    def __init__(self, display_name: Incomplete | None = None, activities: Incomplete | None = None) -> None: ...
