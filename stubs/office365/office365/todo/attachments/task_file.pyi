from typing import AnyStr

from office365.todo.attachments.base import AttachmentBase as AttachmentBase

class TaskFileAttachment(AttachmentBase):
    @property
    def content_bytes(self) -> AnyStr | None: ...
