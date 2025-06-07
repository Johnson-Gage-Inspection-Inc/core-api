from _typeshed import Incomplete
from office365.outlook.calendar.meetingtimes.suggestion import MeetingTimeSuggestion as MeetingTimeSuggestion
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection

class MeetingTimeSuggestionsResult(ClientValue):
    meetingTimeSuggestions: Incomplete
    emptySuggestionsReason: Incomplete
    def __init__(self, meeting_time_suggestions: Incomplete | None = None, empty_suggestions_reason: Incomplete | None = None) -> None: ...
