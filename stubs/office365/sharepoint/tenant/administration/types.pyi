from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class DisableGroupify(ClientValue):
    IsReadOnly: Incomplete
    Value: Incomplete
    def __init__(self, is_read_only: bool = None, value: bool = None) -> None: ...
    @property
    def entity_type_name(self): ...

class EnableAutoNewsDigest(ClientValue):
    IsReadOnly: Incomplete
    Value: Incomplete
    def __init__(self, is_read_only: bool = None, value: bool = None) -> None: ...
    @property
    def entity_type_name(self): ...

class DisableSelfServiceSiteCreation(ClientValue):
    IsReadOnly: Incomplete
    Value: Incomplete
    def __init__(self, is_read_only: bool = None, value: bool = None) -> None: ...
    @property
    def entity_type_name(self): ...

class AutoQuotaEnabled(ClientValue):
    IsReadOnly: Incomplete
    Value: Incomplete
    def __init__(self, is_read_only: Incomplete | None = None, value: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...

class CreatePolicyRequest(ClientValue):
    isPreviewRun: Incomplete
    policyCustomName: Incomplete
    policyDefinitionDetails: Incomplete
    policyDescription: Incomplete
    policyFrequencyUnit: Incomplete
    policyFrequencyValue: Incomplete
    policyId: Incomplete
    policyTags: Incomplete
    policyTemplate: Incomplete
    policyType: Incomplete
    def __init__(self, is_preview_run: Incomplete | None = None, policy_custom_name: Incomplete | None = None, policy_definition_details: Incomplete | None = None, policy_description: Incomplete | None = None, policy_frequency_unit: Incomplete | None = None, policy_frequency_value: Incomplete | None = None, policy_id: Incomplete | None = None, policy_tags: Incomplete | None = None, policy_template: Incomplete | None = None, policy_type: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
