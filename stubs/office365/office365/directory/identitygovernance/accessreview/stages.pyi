from _typeshed import Incomplete
from office365.directory.identitygovernance.accessreview.stage import (
    AccessReviewStage as AccessReviewStage,
)
from office365.entity_collection import EntityCollection as EntityCollection

class AccessReviewStageCollection(EntityCollection[AccessReviewStage]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
