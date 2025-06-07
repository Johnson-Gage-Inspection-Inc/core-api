from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.odata.type import ODataType as ODataType
from office365.sharepoint.search.simple_data_table import SimpleDataTable as SimpleDataTable

class RelevantResults(ClientValue):
    GroupTemplateId: Incomplete
    ItemTemplateId: Incomplete
    Properties: Incomplete
    ResultTitle: Incomplete
    ResultTitleUrl: Incomplete
    RowCount: Incomplete
    Table: Incomplete
    TotalRows: Incomplete
    TotalRowsIncludingDuplicates: Incomplete
    def __init__(self, group_template_id: Incomplete | None = None, item_template_id: Incomplete | None = None, properties: Incomplete | None = None, result_title: Incomplete | None = None, result_title_url: Incomplete | None = None, table=..., row_count: Incomplete | None = None, total_rows: Incomplete | None = None, total_rows_including_duplicates: Incomplete | None = None) -> None: ...
    def set_property(self, k, v, persist_changes: bool = True): ...
    @property
    def entity_type_name(self): ...
