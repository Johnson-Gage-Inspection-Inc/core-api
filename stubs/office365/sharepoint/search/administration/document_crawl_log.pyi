from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.search.simple_data_table import (
    SimpleDataTable as SimpleDataTable,
)

class DocumentCrawlLog(Entity):
    def __init__(self, context) -> None: ...
    def get_crawled_urls(
        self,
        get_count_only: bool = False,
        max_rows: Incomplete | None = None,
        query_string: Incomplete | None = None,
        content_source_id: Incomplete | None = None,
    ): ...
    def get_unsuccesful_crawled_urls(self, display_url: Incomplete | None = None): ...
    @property
    def entity_type_name(self): ...
