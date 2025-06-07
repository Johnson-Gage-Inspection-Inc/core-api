from office365.entity import Entity as Entity
from office365.outlook.mail.messages.rules.actions import (
    MessageRuleActions as MessageRuleActions,
)
from office365.outlook.mail.messages.rules.predicates import (
    MessageRulePredicates as MessageRulePredicates,
)

class MessageRule(Entity):
    @property
    def actions(self): ...
    @property
    def conditions(self): ...
    @property
    def exceptions(self): ...
    @property
    def is_read_only(self) -> bool | None: ...
