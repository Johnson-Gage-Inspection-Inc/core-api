from _typeshed import Incomplete
from office365.runtime.paths.service_operation import (
    ServiceOperationPath as ServiceOperationPath,
)
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection
from office365.sharepoint.fields.related_field import RelatedField as RelatedField

class RelatedFieldCollection(EntityCollection[RelatedField]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def get_by_field_id(self, _id): ...
