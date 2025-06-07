from office365.entity import Entity as Entity
from office365.runtime.types.collections import StringCollection as StringCollection

class ConversationMember(Entity):
    @property
    def display_name(self): ...
    @property
    def roles(self): ...
