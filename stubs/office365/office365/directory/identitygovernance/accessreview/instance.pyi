from office365.directory.identitygovernance.accessreview.stages import (
    AccessReviewStageCollection as AccessReviewStageCollection,
)
from office365.entity import Entity as Entity
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class AccessReviewInstance(Entity):
    @property
    def stages(self) -> AccessReviewStageCollection: ...
