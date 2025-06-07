from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class CallOptions(ClientValue):
    hideBotAfterEscalation: Incomplete
    isContentSharingNotificationEnabled: Incomplete
    def __init__(
        self,
        hide_bot_after_escalation: Incomplete | None = None,
        is_content_sharing_notification_enabled: Incomplete | None = None,
    ) -> None: ...
