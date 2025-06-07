from _typeshed import Incomplete
from office365.entity_collection import EntityCollection as EntityCollection
from office365.todo.attachments.base import AttachmentBase as AttachmentBase

class AttachmentBaseCollection(EntityCollection):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def create_upload_session(self) -> None: ...
