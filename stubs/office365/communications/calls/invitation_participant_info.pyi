from _typeshed import Incomplete
from office365.directory.permissions.identity_set import IdentitySet as IdentitySet
from office365.runtime.client_value import ClientValue as ClientValue

class InvitationParticipantInfo(ClientValue):
    hidden: Incomplete
    identity: Incomplete
    participantId: Incomplete
    removeFromDefaultAudioRoutingGroup: Incomplete
    replacesCallId: Incomplete
    def __init__(self, hidden: Incomplete | None = None, identity=..., participant_id: Incomplete | None = None, remove_from_default_audio_routing_group: Incomplete | None = None, replaces_call_id: Incomplete | None = None) -> None: ...
