from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class TeamMessagingSettings(ClientValue):
    allowUserEditMessages: Incomplete
    allowUserDeleteMessages: Incomplete
    allowOwnerDeleteMessages: Incomplete
    allowTeamMentions: Incomplete
    allowChannelMentions: Incomplete
    def __init__(
        self,
        allow_user_edit_messages: bool = True,
        allow_user_delete_messages: bool = True,
        allow_owner_delete_messages: bool = True,
        allow_team_mentions: bool = True,
        allow_channel_mentions: bool = True,
    ) -> None: ...
