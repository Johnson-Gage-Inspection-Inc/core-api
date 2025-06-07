from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection

class TranslationNotificationRecipient(ClientValue):
    LoginName: Incomplete
    def __init__(self, login_name: Incomplete | None = None) -> None: ...

class TranslationNotificationRecipientCollection(ClientValue):
    LanguageCode: Incomplete
    Recipients: Incomplete
    def __init__(self, language_code: Incomplete | None = None, recipients: Incomplete | None = None) -> None: ...
