from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.search.promoted_results_operations_result import (
    PromotedResultsOperationsResult as PromotedResultsOperationsResult,
)
from office365.sharepoint.search.query.configuration import (
    QueryConfiguration as QueryConfiguration,
)
from office365.sharepoint.search.reports.base import ReportBase as ReportBase

class SearchSetting(Entity):
    def __init__(self, context) -> None: ...
    def get_query_configuration(
        self,
        call_local_search_farms_only: bool = True,
        skip_group_object_id_lookup: Incomplete | None = None,
        throw_on_remote_api_check: Incomplete | None = None,
    ): ...
    def export_search_reports(
        self,
        tenant_id,
        report_type: Incomplete | None = None,
        interval: Incomplete | None = None,
        start_date: Incomplete | None = None,
        end_date: Incomplete | None = None,
        site_collection_id: Incomplete | None = None,
    ): ...
    def ping_admin_endpoint(self): ...
    def get_promoted_result_query_rules(
        self,
        site_collection_level: Incomplete | None = None,
        offset: Incomplete | None = None,
        number_of_rules: Incomplete | None = None,
    ): ...
    @property
    def entity_type_name(self): ...
