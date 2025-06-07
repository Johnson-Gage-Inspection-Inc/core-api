from _typeshed import Incomplete
from office365.entity_collection import EntityCollection as EntityCollection
from office365.onenote.internal.multipart_page_query import OneNotePageCreateQuery as OneNotePageCreateQuery
from office365.onenote.pages.page import OnenotePage as OnenotePage
from typing import IO

class OnenotePageCollection(EntityCollection[OnenotePage]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def add(self, presentation_file: IO, attachment_files: dict = None) -> OnenotePage: ...
