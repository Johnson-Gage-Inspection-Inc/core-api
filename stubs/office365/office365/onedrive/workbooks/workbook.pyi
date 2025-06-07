from _typeshed import Incomplete
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.onedrive.workbooks.applications.application import (
    WorkbookApplication as WorkbookApplication,
)
from office365.onedrive.workbooks.comments.comment import (
    WorkbookComment as WorkbookComment,
)
from office365.onedrive.workbooks.functions.functions import (
    WorkbookFunctions as WorkbookFunctions,
)
from office365.onedrive.workbooks.names.collection import (
    WorkbookNamedItemCollection as WorkbookNamedItemCollection,
)
from office365.onedrive.workbooks.operations.workbook import (
    WorkbookOperation as WorkbookOperation,
)
from office365.onedrive.workbooks.session_info import (
    WorkbookSessionInfo as WorkbookSessionInfo,
)
from office365.onedrive.workbooks.tables.collection import (
    WorkbookTableCollection as WorkbookTableCollection,
)
from office365.onedrive.workbooks.worksheets.collection import (
    WorkbookWorksheetCollection as WorkbookWorksheetCollection,
)
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.http.request_options import RequestOptions as RequestOptions
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.function import FunctionQuery as FunctionQuery
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from typing_extensions import Self

class Workbook(Entity):
    def session_info_resource(self): ...
    def create_session(self, persist_changes: Incomplete | None = None): ...
    def refresh_session(self, session_id: str) -> Self: ...
    def close_session(self, session_id: str) -> Self: ...
    @property
    def application(self): ...
    @property
    def comments(self) -> EntityCollection[WorkbookComment]: ...
    @property
    def functions(self): ...
    @property
    def tables(self) -> WorkbookTableCollection: ...
    @property
    def names(self) -> WorkbookNamedItemCollection: ...
    @property
    def operations(self) -> EntityCollection[WorkbookOperation]: ...
    @property
    def worksheets(self) -> WorkbookWorksheetCollection: ...
