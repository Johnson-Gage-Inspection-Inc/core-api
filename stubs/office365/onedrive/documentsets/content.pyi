from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class DocumentSetContent(ClientValue):
    contentType: Incomplete
    fileName: Incomplete
    folderName: Incomplete
    def __init__(self, content_type: Incomplete | None = None, file_name: Incomplete | None = None, folder_name: Incomplete | None = None) -> None: ...
