from _typeshed import Incomplete
from office365.outlook.calendar.working_hours import WorkingHours as WorkingHours
from office365.outlook.locale_info import LocaleInfo as LocaleInfo
from office365.outlook.mail.automatic_replies_setting import AutomaticRepliesSetting as AutomaticRepliesSetting
from office365.runtime.client_value import ClientValue as ClientValue

class MailboxSettings(ClientValue):
    timeFormat: Incomplete
    timeZone: Incomplete
    automaticRepliesSetting: Incomplete
    archiveFolder: Incomplete
    dateFormat: Incomplete
    language: Incomplete
    workingHours: Incomplete
    def __init__(self, time_format: Incomplete | None = None, time_zone: Incomplete | None = None, automatic_replies_setting=..., archive_folder: Incomplete | None = None, date_format: Incomplete | None = None, language=..., working_hours=...) -> None: ...
