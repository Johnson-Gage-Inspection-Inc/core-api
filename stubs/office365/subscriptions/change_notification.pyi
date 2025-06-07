from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.subscriptions.encrypted_content import ChangeNotificationEncryptedContent as ChangeNotificationEncryptedContent
from office365.subscriptions.resource_data import ResourceData as ResourceData

class ChangeNotification(ClientValue):
    changeType: Incomplete
    clientState: Incomplete
    encryptedContent: Incomplete
    resource: Incomplete
    resourceData: Incomplete
    def __init__(self, change_type: Incomplete | None = None, client_state: Incomplete | None = None, encrypted_content=..., resource: Incomplete | None = None, resource_data=...) -> None: ...
