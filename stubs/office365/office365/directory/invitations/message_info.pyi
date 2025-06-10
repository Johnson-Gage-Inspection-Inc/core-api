from _typeshed import Incomplete
from office365.outlook.mail.recipient import Recipient as Recipient
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)

class InvitedUserMessageInfo(ClientValue):
    ccRecipients: Incomplete
    customizedMessageBody: Incomplete
    messageLanguage: Incomplete
    def __init__(
        self,
        cc_recipients: Incomplete | None = None,
        customized_message_body: Incomplete | None = None,
        message_language: Incomplete | None = None,
    ) -> None: ...
