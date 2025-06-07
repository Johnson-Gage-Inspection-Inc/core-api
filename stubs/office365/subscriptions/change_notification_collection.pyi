from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.runtime.types.collections import StringCollection as StringCollection
from office365.subscriptions.change_notification import ChangeNotification as ChangeNotification

class ChangeNotificationCollection(ClientValue):
    validationTokens: Incomplete
    value: Incomplete
    def __init__(self, validation_tokens: Incomplete | None = None, value: Incomplete | None = None) -> None: ...
