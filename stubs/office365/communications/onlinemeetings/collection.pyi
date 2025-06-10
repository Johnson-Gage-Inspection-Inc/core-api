from _typeshed import Incomplete
from office365.communications.onlinemeetings.online_meeting import (
    OnlineMeeting as OnlineMeeting,
)
from office365.communications.onlinemeetings.recordings.call import (
    CallRecording as CallRecording,
)
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.queries.create_entity import (
    CreateEntityQuery as CreateEntityQuery,
)
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)

class OnlineMeetingCollection(EntityCollection[OnlineMeeting]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def create(
        self,
        subject,
        start_datetime: Incomplete | None = None,
        end_datetime: Incomplete | None = None,
    ): ...
    def create_or_get(
        self,
        external_id: Incomplete | None = None,
        start_datetime: Incomplete | None = None,
        end_datetime: Incomplete | None = None,
        subject: Incomplete | None = None,
        participants: Incomplete | None = None,
        chat_info: Incomplete | None = None,
    ): ...
    def get_all_recordings(
        self,
        meeting_organizer_user_id,
        start_datetime: Incomplete | None = None,
        end_datetime: Incomplete | None = None,
    ): ...
