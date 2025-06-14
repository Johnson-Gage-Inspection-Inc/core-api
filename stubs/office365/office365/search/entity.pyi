from _typeshed import Incomplete
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.paths.v4.entity import EntityPath as EntityPath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.search.acronyms.acronym import Acronym as Acronym
from office365.search.bookmarks.bookmark import Bookmark as Bookmark
from office365.search.entity_type import EntityType as EntityType
from office365.search.hit import SearchHit as SearchHit
from office365.search.qnas.qna import Qna as Qna
from office365.search.query import SearchQuery as SearchQuery
from office365.search.request import SearchRequest as SearchRequest
from office365.search.response import SearchResponse as SearchResponse

class SearchEntity(Entity):
    def query(
        self,
        query_string: str,
        entity_types: list[str] | None = None,
        page_from: int | None = None,
        size: int | None = None,
        enable_top_results: bool | None = None,
        region: str | None = None,
    ) -> ClientResult[ClientValueCollection[SearchResponse]]: ...
    def query_messages(
        self,
        query_string,
        page_from: Incomplete | None = None,
        size: Incomplete | None = None,
        enable_top_results: Incomplete | None = None,
    ): ...
    def query_events(self, query_string): ...
    def query_drive_items(
        self,
        query_string,
        page_from: Incomplete | None = None,
        size: Incomplete | None = None,
    ): ...
    def query_list_items(
        self,
        query_string,
        page_from: Incomplete | None = None,
        size: Incomplete | None = None,
        region: Incomplete | None = None,
    ): ...
    def query_peoples(
        self,
        query_string,
        page_from: Incomplete | None = None,
        size: Incomplete | None = None,
        region: Incomplete | None = None,
    ): ...
    def query_sites(
        self,
        query_string,
        page_from: Incomplete | None = None,
        size: Incomplete | None = None,
        region: Incomplete | None = None,
    ): ...
    @property
    def acronyms(self): ...
    @property
    def bookmarks(self): ...
    @property
    def qnas(self): ...
