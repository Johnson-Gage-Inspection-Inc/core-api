from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.teams.teamwork.user_identity import (
    TeamworkUserIdentity as TeamworkUserIdentity,
)

class TeamworkOnlineMeetingInfo(ClientValue):
    calendarEventId: Incomplete
    joinWebUrl: Incomplete
    organizer: Incomplete
    def __init__(
        self,
        calendar_event_id: Incomplete | None = None,
        join_web_url: Incomplete | None = None,
        organizer=...,
    ) -> None: ...
