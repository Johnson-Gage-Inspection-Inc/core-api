from _typeshed import Incomplete
from office365.entity_collection import EntityCollection as EntityCollection
from office365.onenote.entity_hierarchy_model import (
    OnenoteEntityHierarchyModel as OnenoteEntityHierarchyModel,
)
from office365.onenote.notebooks.notebook import Notebook as Notebook
from office365.onenote.sections.section import OnenoteSection as OnenoteSection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class SectionGroup(OnenoteEntityHierarchyModel):
    @property
    def section_groups_url(self) -> str | None: ...
    @property
    def sections_url(self) -> str | None: ...
    @property
    def parent_notebook(self) -> Notebook: ...
    @property
    def sections(self) -> EntityCollection[OnenoteSection]: ...
    @property
    def section_groups(self) -> EntityCollection[SectionGroup]: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
