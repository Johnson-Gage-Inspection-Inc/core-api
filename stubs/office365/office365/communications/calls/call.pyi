from _typeshed import Incomplete
from office365.communications.calls.incoming_context import (
    IncomingContext as IncomingContext,
)
from office365.communications.calls.participant import Participant as Participant
from office365.communications.calls.route import CallRoute as CallRoute
from office365.communications.operations.cancel_media_processing import (
    CancelMediaProcessingOperation as CancelMediaProcessingOperation,
)
from office365.communications.operations.comms import CommsOperation as CommsOperation
from office365.communications.operations.unmute_participant import (
    UnmuteParticipantOperation as UnmuteParticipantOperation,
)
from office365.communications.operations.update_recording_status import (
    UpdateRecordingStatusOperation as UpdateRecordingStatusOperation,
)
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)

class Call(Entity):
    def cancel_media_processing(self, client_context: Incomplete | None = None): ...
    def reject(
        self, reason: Incomplete | None = None, callback_uri: Incomplete | None = None
    ): ...
    def delete(self): ...
    def update_recording_status(self, status, client_context): ...
    def unmute(self, client_context): ...
    @property
    def callback_uri(self): ...
    @property
    def call_routes(self): ...
    @property
    def incoming_context(self): ...
    @property
    def participants(self): ...
    @property
    def operations(self): ...
