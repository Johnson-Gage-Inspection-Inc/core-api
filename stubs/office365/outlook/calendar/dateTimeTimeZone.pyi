from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class DateTimeTimeZone(ClientValue):
    dateTime: Incomplete
    timeZone: Incomplete
    def __init__(self, datetime: Incomplete | None = None, timezone: Incomplete | None = None) -> None: ...
    @staticmethod
    def parse(dt): ...
