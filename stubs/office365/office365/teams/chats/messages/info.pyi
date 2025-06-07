from office365.entity import Entity as Entity
from office365.outlook.mail.item_body import ItemBody as ItemBody

class ChatMessageInfo(Entity):
    @property
    def body(self): ...
    @property
    def created_datetime(self): ...
