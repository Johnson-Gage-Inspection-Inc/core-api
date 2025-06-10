from office365.todo.attachments.base import AttachmentBase as AttachmentBase
from typing import AnyStr

class TaskFileAttachment(AttachmentBase):
    @property
    def content_bytes(self) -> AnyStr | None: ...
