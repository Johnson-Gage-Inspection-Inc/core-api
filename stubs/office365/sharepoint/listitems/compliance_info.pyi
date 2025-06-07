from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class ListItemComplianceInfo(ClientValue):
    ComplianceTag: Incomplete
    TagPolicyEventBased: Incomplete
    TagPolicyHold: Incomplete
    TagPolicyRecord: Incomplete
    def __init__(self, compliance_tag: Incomplete | None = None, tag_policy_event_based: Incomplete | None = None, tag_policy_hold: Incomplete | None = None, tag_policy_record: Incomplete | None = None) -> None: ...
