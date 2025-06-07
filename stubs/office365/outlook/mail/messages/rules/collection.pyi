from _typeshed import Incomplete
from office365.entity_collection import EntityCollection as EntityCollection
from office365.outlook.mail.messages.rules.rule import MessageRule as MessageRule

class MessageRuleCollection(EntityCollection[MessageRule]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def add(self, display_name, sequence, actions, **kwargs): ...
