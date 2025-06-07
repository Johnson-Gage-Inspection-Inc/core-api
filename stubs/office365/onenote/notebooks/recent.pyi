from _typeshed import Incomplete
from office365.onenote.notebooks.recent_links import RecentNotebookLinks as RecentNotebookLinks
from office365.runtime.client_value import ClientValue as ClientValue

class RecentNotebook(ClientValue):
    displayName: Incomplete
    links: Incomplete
    def __init__(self, display_name: Incomplete | None = None, links=...) -> None: ...
