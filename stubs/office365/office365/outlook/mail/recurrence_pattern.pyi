from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.types.collections import StringCollection as StringCollection

class RecurrencePattern(ClientValue):
    dayOfMonth: Incomplete
    daysOfWeek: Incomplete
    firstDayOfWeek: Incomplete
    index: Incomplete
    interval: Incomplete
    month: Incomplete
    type: Incomplete
    def __init__(
        self,
        day_of_month: Incomplete | None = None,
        days_of_week: Incomplete | None = None,
        first_day_of_week: Incomplete | None = None,
        index: Incomplete | None = None,
        interval: Incomplete | None = None,
        month: Incomplete | None = None,
        pattern_type: Incomplete | None = None,
    ) -> None: ...
