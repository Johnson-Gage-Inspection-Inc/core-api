from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class ComplianceTagInfo(ClientValue):
    IsRecord: Incomplete
    IsRegulatory: Incomplete
    ShouldKeep: Incomplete
    TagName: Incomplete
    UnifiedRuleId: Incomplete
    UnifiedTagId: Incomplete
    def __init__(
        self,
        is_record: Incomplete | None = None,
        is_regulatory: Incomplete | None = None,
        should_keep: Incomplete | None = None,
        tag_name: Incomplete | None = None,
        unified_rule_id: Incomplete | None = None,
        unified_tag_id: Incomplete | None = None,
    ) -> None: ...
    @property
    def entity_type_name(self): ...
