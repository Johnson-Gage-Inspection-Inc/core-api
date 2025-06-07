from _typeshed import Incomplete
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.onenote.notebooks.collection import (
    NotebookCollection as NotebookCollection,
)
from office365.onenote.operations.onenote import OnenoteOperation as OnenoteOperation
from office365.onenote.pages.collection import (
    OnenotePageCollection as OnenotePageCollection,
)
from office365.onenote.resources.resource import OnenoteResource as OnenoteResource
from office365.onenote.sectiongroups.section_group import SectionGroup as SectionGroup
from office365.onenote.sections.section import OnenoteSection as OnenoteSection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class Onenote(Entity):
    @property
    def notebooks(self) -> NotebookCollection: ...
    @property
    def operations(self): ...
    @property
    def pages(self) -> OnenotePageCollection: ...
    @property
    def resources(self): ...
    @property
    def sections(self) -> EntityCollection[OnenoteSection]: ...
    @property
    def section_groups(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
