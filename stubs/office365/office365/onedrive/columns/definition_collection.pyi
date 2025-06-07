from _typeshed import Incomplete
from office365.entity_collection import EntityCollection as EntityCollection
from office365.onedrive.columns.definition import ColumnDefinition as ColumnDefinition
from office365.onedrive.lists.list import List as List
from office365.runtime.queries.create_entity import (
    CreateEntityQuery as CreateEntityQuery,
)

class ColumnDefinitionCollection(EntityCollection[ColumnDefinition]):
    def __init__(self, context, resource_path, parent) -> None: ...
    def add_number(
        self, name, minimum: Incomplete | None = None, maximum: Incomplete | None = None
    ): ...
    def add_text(
        self,
        name,
        max_length: Incomplete | None = None,
        text_type: Incomplete | None = None,
    ): ...
    def add_hyperlink_or_picture(self, name, is_picture: Incomplete | None = None): ...
    def add_lookup(
        self, name: str, lookup_list: List | str, column_name: str | None = None
    ) -> ColumnDefinition: ...
