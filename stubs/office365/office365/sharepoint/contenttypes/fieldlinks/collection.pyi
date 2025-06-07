from _typeshed import Incomplete
from office365.runtime.paths.service_operation import (
    ServiceOperationPath as ServiceOperationPath,
)
from office365.runtime.queries.create_entity import (
    CreateEntityQuery as CreateEntityQuery,
)
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.runtime.types.collections import StringCollection as StringCollection
from office365.sharepoint.contenttypes.fieldlinks.field_link import (
    FieldLink as FieldLink,
)
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection
from office365.sharepoint.fields.field import Field as Field
from typing_extensions import Self

class FieldLinkCollection(EntityCollection[FieldLink]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def add(self, field): ...
    def get_by_id(self, _id): ...
    def reorder(self, internal_names: list[str]) -> Self: ...
