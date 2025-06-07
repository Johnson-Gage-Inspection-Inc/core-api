from _typeshed import Incomplete
from office365.onedrive.folders.view import FolderView as FolderView
from office365.runtime.client_value import ClientValue as ClientValue

class Folder(ClientValue):
    childCount: Incomplete
    view: Incomplete
    def __init__(self, child_count: Incomplete | None = None, view=...) -> None: ...
