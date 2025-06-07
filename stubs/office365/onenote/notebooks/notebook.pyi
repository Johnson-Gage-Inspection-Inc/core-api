from _typeshed import Incomplete
from office365.entity_collection import EntityCollection as EntityCollection
from office365.onenote.entity_hierarchy_model import OnenoteEntityHierarchyModel as OnenoteEntityHierarchyModel
from office365.onenote.sections.section import OnenoteSection as OnenoteSection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class Notebook(OnenoteEntityHierarchyModel):
    @property
    def sections(self) -> EntityCollection[OnenoteSection]: ...
    @property
    def section_groups(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
