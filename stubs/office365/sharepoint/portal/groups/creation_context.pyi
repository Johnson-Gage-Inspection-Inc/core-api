from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class GroupCreationContext(ClientValue):
    PreferredLanguage: Incomplete
    SensitivityLabelPolicyMandatory: Incomplete
    SitePath: Incomplete
    def __init__(self, preferred_language: Incomplete | None = None, sensitivity_label_policy_mandatory: Incomplete | None = None, site_path: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
