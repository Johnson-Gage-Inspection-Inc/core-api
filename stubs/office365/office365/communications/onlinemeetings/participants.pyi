from _typeshed import Incomplete
from office365.communications.onlinemeetings.participant_info import (
    MeetingParticipantInfo as MeetingParticipantInfo,
)
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)

class MeetingParticipants(ClientValue):
    organizer: Incomplete
    attendees: Incomplete
    def __init__(self, organizer=..., attendees: Incomplete | None = None) -> None: ...
