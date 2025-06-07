from _typeshed import Incomplete
from office365.outlook.calendar.dateTimeTimeZone import DateTimeTimeZone as DateTimeTimeZone
from office365.outlook.locale_info import LocaleInfo as LocaleInfo
from office365.runtime.client_value import ClientValue as ClientValue

class AutomaticRepliesMailTips(ClientValue):
    message: Incomplete
    messageLanguage: Incomplete
    scheduledEndTime: Incomplete
    scheduledStartTime: Incomplete
    def __init__(self, message: Incomplete | None = None, message_language=..., scheduled_end_time=..., scheduled_start_time=...) -> None: ...
