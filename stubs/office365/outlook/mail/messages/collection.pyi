from _typeshed import Incomplete
from office365.delta_collection import DeltaCollection as DeltaCollection
from office365.outlook.mail.item_body import ItemBody as ItemBody
from office365.outlook.mail.messages.message import Message as Message
from office365.outlook.mail.recipient import Recipient as Recipient
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection

class MessageCollection(DeltaCollection[Message]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def add(self, subject: Incomplete | None = None, body: Incomplete | None = None, to_recipients: Incomplete | None = None, **kwargs): ...
