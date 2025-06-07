from office365.communications.calls.invitation_participant_info import (
    InvitationParticipantInfo as InvitationParticipantInfo,
)
from office365.communications.operations.comms import CommsOperation as CommsOperation
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)

class InviteParticipantsOperation(CommsOperation):
    @property
    def participants(self): ...
