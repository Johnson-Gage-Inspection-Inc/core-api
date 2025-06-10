from _typeshed import Incomplete
from office365.runtime.paths.service_operation import (
    ServiceOperationPath as ServiceOperationPath,
)
from office365.sharepoint.contentcenter.machinelearning.models.model import (
    SPMachineLearningModel as SPMachineLearningModel,
)
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection

class SPMachineLearningModelCollection(EntityCollection[SPMachineLearningModel]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def get_by_title(self, title): ...
