from _typeshed import Incomplete
from office365.entity_collection import EntityCollection as EntityCollection
from office365.onenote.notebooks.copy_notebook_model import CopyNotebookModel as CopyNotebookModel
from office365.onenote.notebooks.notebook import Notebook as Notebook
from office365.onenote.notebooks.recent import RecentNotebook as RecentNotebook
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.runtime.queries.function import FunctionQuery as FunctionQuery
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery

class NotebookCollection(EntityCollection[Notebook]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def add(self, display_name): ...
    def get_notebook_from_web_url(self, web_url): ...
    def get_recent_notebooks(self, include_personal_notebooks: bool = True): ...
