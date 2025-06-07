from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class SiteHealthResult(ClientValue):
    MessageAsText: Incomplete
    RuleHelpLink: Incomplete
    RuleId: Incomplete
    def __init__(self, message_as_text: Incomplete | None = None, rule_help_link: Incomplete | None = None, rule_id: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
