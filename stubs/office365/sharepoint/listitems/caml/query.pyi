from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.sharepoint.listitems.collection_position import ListItemCollectionPosition as ListItemCollectionPosition
from office365.sharepoint.views.scope import ViewScope as ViewScope

class WhereElement: ...
class OrderByElement: ...
class GroupByElement: ...

class QueryElement:
    Where: Incomplete
    OrderBy: Incomplete
    GroupBy: Incomplete
    def __init__(self) -> None: ...
    @staticmethod
    def parse(expr): ...

class RowLimitElement:
    Top: Incomplete
    def __init__(self, top: Incomplete | None = None) -> None: ...

class ViewElement:
    Scope: Incomplete
    Query: Incomplete
    RowLimit: Incomplete
    def __init__(self, scope=..., query=..., row_limit=...) -> None: ...

class CamlQuery(ClientValue):
    DatesInUtc: Incomplete
    FolderServerRelativeUrl: Incomplete
    AllowIncrementalResults: Incomplete
    ViewXml: Incomplete
    ListItemCollectionPosition: Incomplete
    def __init__(self, dates_in_utc: bool = True, view_xml: Incomplete | None = None, list_item_collection_position: Incomplete | None = None, folder_server_relative_url: Incomplete | None = None, allow_incremental_results: bool = True) -> None: ...
    @staticmethod
    def parse(query_expr, scope=...): ...
    @staticmethod
    def create_all_items_query(): ...
    @staticmethod
    def create_all_folders_query(): ...
    @staticmethod
    def create_all_files_query(): ...
    @property
    def entity_type_name(self): ...
