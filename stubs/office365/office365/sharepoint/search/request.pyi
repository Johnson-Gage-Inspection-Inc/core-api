from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.types.collections import StringCollection as StringCollection
from office365.sharepoint.search.query.property import QueryProperty as QueryProperty
from office365.sharepoint.search.query.reordering_rule import (
    ReorderingRule as ReorderingRule,
)
from office365.sharepoint.search.query.sort.sort import Sort as Sort

class SearchRequest(ClientValue):
    Querytext: Incomplete
    SelectProperties: Incomplete
    ClientType: Incomplete
    CollapseSpecification: Incomplete
    Culture: Incomplete
    EnableSorting: Incomplete
    SortList: Incomplete
    TrimDuplicates: Incomplete
    RankingModelId: Incomplete
    RowLimit: Incomplete
    RowsPerPage: Incomplete
    QueryTemplate: Incomplete
    SummaryLength: Incomplete
    StartRow: Incomplete
    EnableQueryRules: Incomplete
    SourceId: Incomplete
    ReorderingRules: Incomplete
    Properties: Incomplete
    UILanguage: Incomplete
    HitHighlightedProperties: Incomplete
    HitHighlightedMultivaluePropertyLimit: Incomplete
    def __init__(
        self,
        query_text,
        select_properties: Incomplete | None = None,
        culture: Incomplete | None = None,
        trim_duplicates: bool = False,
        row_limit: Incomplete | None = None,
        rows_per_page: Incomplete | None = None,
        start_row: Incomplete | None = None,
        enable_sorting: Incomplete | None = None,
        sort_list: Incomplete | None = None,
        query_template: Incomplete | None = None,
        ranking_model_id: Incomplete | None = None,
        summary_length: Incomplete | None = None,
        collapse_specification: Incomplete | None = None,
        client_type: Incomplete | None = None,
        enable_query_rules: Incomplete | None = None,
        source_id: Incomplete | None = None,
        reordering_rules: Incomplete | None = None,
        properties: Incomplete | None = None,
        ui_language: Incomplete | None = None,
        hit_highlighted_properties: Incomplete | None = None,
        hit_highlighted_multivalue_property_limit: Incomplete | None = None,
        **kwargs,
    ) -> None: ...
    @property
    def entity_type_name(self): ...
