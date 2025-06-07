from _typeshed import Incomplete
from office365.outlook.calendar.sharing.message_action import CalendarSharingMessageAction as CalendarSharingMessageAction
from office365.outlook.mail.messages.message import Message as Message

class CalendarSharingMessage(Message):
    @property
    def sharing_message_action(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
