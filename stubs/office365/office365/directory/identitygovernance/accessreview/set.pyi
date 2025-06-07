from _typeshed import Incomplete
from office365.directory.identitygovernance.accessreview.history.definition import (
    AccessReviewHistoryDefinition as AccessReviewHistoryDefinition,
)
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class AccessReviewSet(Entity):
    @property
    def history_definitions(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
