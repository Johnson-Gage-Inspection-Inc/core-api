from _typeshed import Incomplete
from office365.outlook.calendar.dateTimeTimeZone import DateTimeTimeZone as DateTimeTimeZone
from office365.runtime.client_value import ClientValue as ClientValue

class AutomaticRepliesSetting(ClientValue):
    externalAudience: Incomplete
    externalReplyMessage: Incomplete
    internalReplyMessage: Incomplete
    scheduledEndDateTime: Incomplete
    scheduledStartDateTime: Incomplete
    status: Incomplete
    def __init__(self, external_audience: Incomplete | None = None, external_reply_message: Incomplete | None = None, internal_reply_message: Incomplete | None = None, scheduled_end_datetime=..., scheduled_start_datetime=..., status: Incomplete | None = None) -> None: ...
