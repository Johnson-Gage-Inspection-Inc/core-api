from _typeshed import Incomplete
from datetime import datetime
from office365.communications.onlinemeetings.participants import (
    MeetingParticipants as MeetingParticipants,
)
from office365.communications.onlinemeetings.recordings.call import (
    CallRecording as CallRecording,
)
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.outlook.mail.item_body import ItemBody as ItemBody
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.function import FunctionQuery as FunctionQuery
from office365.runtime.types.collections import StringCollection as StringCollection
from typing import AnyStr

class OnlineMeeting(Entity):
    def get_virtual_appointment_join_web_url(self): ...
    @property
    def allow_attendee_to_enable_camera(self) -> bool | None: ...
    @property
    def allow_attendee_to_enable_mic(self) -> bool | None: ...
    @property
    def allowed_presenters(self): ...
    @property
    def allow_meeting_chat(self) -> bool | None: ...
    @property
    def allow_participants_to_change_name(self) -> bool | None: ...
    @property
    def attendee_report(self) -> AnyStr | None: ...
    @property
    def participants(self): ...
    @property
    def subject(self) -> str | None: ...
    @subject.setter
    def subject(self, value: str) -> None: ...
    @property
    def start_datetime(self): ...
    @start_datetime.setter
    def start_datetime(self, value: datetime) -> None: ...
    @property
    def end_datetime(self): ...
    @end_datetime.setter
    def end_datetime(self, value: datetime) -> None: ...
    @property
    def join_information(self): ...
    @property
    def join_web_url(self) -> str | None: ...
    @property
    def video_teleconference_id(self) -> str | None: ...
    @property
    def recordings(self) -> EntityCollection[CallRecording]: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
