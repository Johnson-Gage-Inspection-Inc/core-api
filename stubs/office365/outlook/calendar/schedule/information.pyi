from _typeshed import Incomplete
from office365.outlook.calendar.schedule.item import ScheduleItem as ScheduleItem
from office365.outlook.calendar.working_hours import WorkingHours as WorkingHours
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection

class ScheduleInformation(ClientValue):
    scheduleItems: Incomplete
    scheduleId: Incomplete
    availabilityView: Incomplete
    error: Incomplete
    workingHours: Incomplete
    def __init__(self, schedule_id: Incomplete | None = None, schedule_items: Incomplete | None = None, availability_view: Incomplete | None = None, error: Incomplete | None = None, working_hours=...) -> None: ...
