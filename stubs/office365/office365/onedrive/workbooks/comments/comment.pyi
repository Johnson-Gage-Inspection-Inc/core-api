from typing import AnyStr

from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.onedrive.workbooks.comments.reply import (
    WorkbookCommentReply as WorkbookCommentReply,
)
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class WorkbookComment(Entity):
    @property
    def content(self) -> AnyStr | None: ...
    @property
    def content_type(self) -> str | None: ...
    @property
    def replies(self) -> EntityCollection[WorkbookCommentReply]: ...
