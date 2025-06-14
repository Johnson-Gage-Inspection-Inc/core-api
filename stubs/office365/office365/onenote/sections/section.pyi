from _typeshed import Incomplete
from office365.entity_collection import EntityCollection as EntityCollection
from office365.onenote.entity_hierarchy_model import (
    OnenoteEntityHierarchyModel as OnenoteEntityHierarchyModel,
)
from office365.onenote.operations.onenote import OnenoteOperation as OnenoteOperation
from office365.onenote.pages.links import PageLinks as PageLinks
from office365.onenote.pages.page import OnenotePage as OnenotePage
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)

class OnenoteSection(OnenoteEntityHierarchyModel):
    def copy_to_section_group(
        self,
        group_id,
        _id,
        rename_as: Incomplete | None = None,
        site_collection_id: Incomplete | None = None,
        site_id: Incomplete | None = None,
    ): ...
    @property
    def is_default(self) -> bool | None: ...
    @property
    def links(self): ...
    @property
    def pages(self) -> EntityCollection[OnenotePage]: ...
    @property
    def parent_notebook(self): ...
    @property
    def parent_section_group(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
