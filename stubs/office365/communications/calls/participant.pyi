from _typeshed import Incomplete
from office365.communications.calls.invitation_participant_info import InvitationParticipantInfo as InvitationParticipantInfo
from office365.communications.calls.participant_info import ParticipantInfo as ParticipantInfo
from office365.communications.onlinemeetings.restricted import OnlineMeetingRestricted as OnlineMeetingRestricted
from office365.communications.operations.invite_participants import InviteParticipantsOperation as InviteParticipantsOperation
from office365.communications.operations.start_hold_music import StartHoldMusicOperation as StartHoldMusicOperation
from office365.communications.operations.stop_hold_music import StopHoldMusicOperation as StopHoldMusicOperation
from office365.entity import Entity as Entity
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery

class Participant(Entity):
    def invite(self, participants, client_context): ...
    def start_hold_music(self, custom_prompt: Incomplete | None = None, client_context: Incomplete | None = None): ...
    def stop_hold_music(self, client_context: Incomplete | None = None): ...
    @property
    def info(self): ...
    @property
    def metadata(self) -> str | None: ...
    @property
    def restricted_experience(self): ...
