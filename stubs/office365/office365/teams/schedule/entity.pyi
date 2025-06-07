from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class ScheduleEntity(ClientValue):
    endDateTime: Incomplete
    def __init__(self, end_datetime: Incomplete | None = None) -> None: ...
