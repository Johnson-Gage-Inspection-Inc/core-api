from _typeshed import Incomplete
from office365.outlook.mail.recurrence_pattern import RecurrencePattern as RecurrencePattern
from office365.outlook.mail.recurrence_range import RecurrenceRange as RecurrenceRange
from office365.runtime.client_value import ClientValue as ClientValue

class PatternedRecurrence(ClientValue):
    pattern: Incomplete
    range: Incomplete
    def __init__(self, pattern=..., recurrence_range=...) -> None: ...
