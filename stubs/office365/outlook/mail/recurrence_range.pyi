import datetime

from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class RecurrenceRange(ClientValue):
    endDate: Incomplete
    numberOfOccurrences: Incomplete
    recurrenceTimeZone: Incomplete
    startDate: Incomplete
    type: Incomplete
    def __init__(
        self,
        start_date: datetime.date | None = None,
        end_date: datetime.date | None = None,
        number_of_occurrences: int | None = None,
        recurrence_timezone: str | None = None,
        range_type: str | None = None,
    ) -> None: ...
