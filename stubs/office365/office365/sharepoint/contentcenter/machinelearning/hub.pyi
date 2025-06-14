from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.compliance.tag import ComplianceTag as ComplianceTag
from office365.sharepoint.contentcenter.machinelearning.enabled import (
    SPMachineLearningEnabled as SPMachineLearningEnabled,
)
from office365.sharepoint.contentcenter.machinelearning.models.collection import (
    SPMachineLearningModelCollection as SPMachineLearningModelCollection,
)
from office365.sharepoint.contentcenter.machinelearning.samples.collection import (
    SPMachineLearningSampleCollection as SPMachineLearningSampleCollection,
)
from office365.sharepoint.contentcenter.syntex_models_landing_info import (
    SyntexModelsLandingInfo as SyntexModelsLandingInfo,
)
from office365.sharepoint.entity import Entity as Entity

class SPMachineLearningHub(Entity):
    def get_by_content_type_id(self, content_type_id): ...
    def get_models(
        self,
        list_id: Incomplete | None = None,
        model_types: Incomplete | None = None,
        publication_types: Incomplete | None = None,
        include_management_not_allowed_models: Incomplete | None = None,
    ): ...
    def get_retention_labels(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
    @property
    def is_default_content_center(self) -> bool | None: ...
    @property
    def machine_learning_capture_enabled(self) -> bool | None: ...
    @property
    def machine_learning_enabled(self): ...
    @property
    def models(self): ...
    @property
    def samples(self): ...
    @property
    def entity_type_name(self): ...
