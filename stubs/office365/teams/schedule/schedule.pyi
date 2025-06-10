from _typeshed import Incomplete
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.teams.schedule.groups.group import SchedulingGroup as SchedulingGroup
from office365.teams.schedule.shifts.open.change_request import (
    OpenShiftChangeRequest as OpenShiftChangeRequest,
)
from office365.teams.schedule.shifts.shift import Shift as Shift
from office365.teams.schedule.time_off_reason import TimeOffReason as TimeOffReason

class Schedule(Entity):
    @property
    def time_zone(self): ...
    @time_zone.setter
    def time_zone(self, value) -> None: ...
    @property
    def open_shift_change_requests(
        self,
    ) -> EntityCollection[OpenShiftChangeRequest]: ...
    @property
    def shifts(self) -> EntityCollection[Shift]: ...
    @property
    def scheduling_groups(self) -> EntityCollection[SchedulingGroup]: ...
    @property
    def time_off_reasons(self) -> EntityCollection[TimeOffReason]: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
