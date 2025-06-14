from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.function import FunctionQuery as FunctionQuery
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.runtime.types.collections import StringCollection as StringCollection
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.principal.users.user import User as User
from office365.sharepoint.search.query.auto_completion_results import (
    QueryAutoCompletionResults as QueryAutoCompletionResults,
)
from office365.sharepoint.search.query.popular_tenant_query import (
    PopularTenantQuery as PopularTenantQuery,
)
from office365.sharepoint.search.query.sort.sort import Sort as Sort
from office365.sharepoint.search.query.suggestion_results import (
    QuerySuggestionResults as QuerySuggestionResults,
)
from office365.sharepoint.search.query.tenant_custom_query_suggestions import (
    TenantCustomQuerySuggestions as TenantCustomQuerySuggestions,
)
from office365.sharepoint.search.request import SearchRequest as SearchRequest
from office365.sharepoint.search.result import SearchResult as SearchResult
from typing import Any

class SearchService(Entity):
    def __init__(self, context) -> None: ...
    def export(self, user, start_time): ...
    def export_manual_suggestions(self): ...
    def export_popular_tenant_queries(self, count): ...
    def query(
        self,
        query_text,
        source_id: Incomplete | None = None,
        ranking_model_id: Incomplete | None = None,
        start_row: Incomplete | None = None,
        row_limit: Incomplete | None = None,
        rows_per_page: Incomplete | None = None,
        select_properties: Incomplete | None = None,
        refinement_filters: Incomplete | None = None,
        refiners: Incomplete | None = None,
        sort_list: Incomplete | None = None,
        trim_duplicates: Incomplete | None = None,
        enable_query_rules: Incomplete | None = None,
        enable_sorting: Incomplete | None = None,
        **kwargs,
    ): ...
    def post_query(
        self,
        query_text: str,
        select_properties: list[str] = None,
        trim_duplicates: bool = None,
        row_limit: int = None,
        **kwargs: Any,
    ) -> ClientResult[SearchResult]: ...
    def record_page_click(
        self,
        page_info: Incomplete | None = None,
        click_type: Incomplete | None = None,
        block_type: Incomplete | None = None,
    ): ...
    def search_center_url(self) -> ClientResult[str]: ...
    def results_page_address(self): ...
    def suggest(self, query_text): ...
    def auto_completions(
        self,
        query_text,
        sources: Incomplete | None = None,
        number_of_completions: Incomplete | None = None,
        cursor_position: Incomplete | None = None,
    ): ...
