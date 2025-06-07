from _typeshed import Incomplete
from office365.outlook.calendar.dateTimeTimeZone import DateTimeTimeZone as DateTimeTimeZone
from office365.runtime.client_value import ClientValue as ClientValue

class FollowupFlag(ClientValue):
    completedDateTime: Incomplete
    dueDateTime: Incomplete
    flagStatus: Incomplete
    startDateTime: Incomplete
    def __init__(self, completed_datetime=..., due_datetime=..., flag_status: Incomplete | None = None, start_datetime=...) -> None: ...
