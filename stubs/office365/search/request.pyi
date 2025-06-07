from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.runtime.odata.json_format import ODataJsonFormat as ODataJsonFormat
from office365.runtime.types.collections import StringCollection as StringCollection
from office365.search.aggregation_option import AggregationOption as AggregationOption
from office365.search.sharepoint_onedrive_options import SharePointOneDriveOptions as SharePointOneDriveOptions
from office365.search.sort_property import SortProperty as SortProperty

class SearchRequest(ClientValue):
    query: Incomplete
    aggregationFilters: Incomplete
    aggregations: Incomplete
    enableTopResults: Incomplete
    size: Incomplete
    region: Incomplete
    entityTypes: Incomplete
    fields: Incomplete
    page_from: Incomplete
    sortProperties: Incomplete
    contentSources: Incomplete
    sharePointOneDriveOptions: Incomplete
    def __init__(self, query, aggregation_filters: Incomplete | None = None, aggregations: Incomplete | None = None, enable_top_results: Incomplete | None = None, size: Incomplete | None = None, region: Incomplete | None = None, entity_types: Incomplete | None = None, fields: Incomplete | None = None, page_from: Incomplete | None = None, sort_properties: Incomplete | None = None, content_sources: Incomplete | None = None, sharepoint_onedrive_options=...) -> None: ...
    def to_json(self, json_format: ODataJsonFormat | None = None) -> dict: ...
