from _typeshed import Incomplete
from office365.onenote.entity_schema_object_model import (
    OnenoteEntitySchemaObjectModel as OnenoteEntitySchemaObjectModel,
)
from office365.onenote.notebooks.notebook import Notebook as Notebook
from office365.onenote.pages.links import PageLinks as PageLinks
from office365.onenote.sections.section import OnenoteSection as OnenoteSection
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.function import FunctionQuery as FunctionQuery
from office365.runtime.types.collections import StringCollection as StringCollection
from typing import AnyStr

class OnenotePage(OnenoteEntitySchemaObjectModel):
    def get_content(self) -> ClientResult[AnyStr]: ...
    @property
    def content_url(self) -> str | None: ...
    @property
    def links(self): ...
    @property
    def title(self) -> str | None: ...
    @property
    def user_tags(self): ...
    @property
    def parent_notebook(self): ...
    @property
    def parent_section(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
