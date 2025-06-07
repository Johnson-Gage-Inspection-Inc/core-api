from office365.outlook.mail.messages.message import Message as Message
from office365.outlook.mail.patterned_recurrence import PatternedRecurrence as PatternedRecurrence
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class EventMessage(Message):
    @property
    def event(self): ...
    @property
    def patterned_recurrence(self): ...
