from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class AttachmentItem(ClientValue):
    attachmentType: Incomplete
    name: Incomplete
    size: Incomplete
    def __init__(
        self,
        attachment_type: Incomplete | None = None,
        name: Incomplete | None = None,
        size: Incomplete | None = None,
    ) -> None: ...
    @staticmethod
    def create_file(path): ...
