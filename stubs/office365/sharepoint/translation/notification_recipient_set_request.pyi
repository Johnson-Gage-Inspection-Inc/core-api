from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.sharepoint.translation.notification_recipient import TranslationNotificationRecipientCollection as TranslationNotificationRecipientCollection

class TranslationNotificationRecipientSetRequest(ClientValue):
    NotificationRecipients: Incomplete
    def __init__(self, notification_recipients: Incomplete | None = None) -> None: ...
