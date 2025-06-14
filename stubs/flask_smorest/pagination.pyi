import marshmallow as ma
from _typeshed import Incomplete

from .utils import unpack_tuple_response as unpack_tuple_response

class PaginationParameters:
    page: Incomplete
    page_size: Incomplete
    item_count: Incomplete
    def __init__(self, page, page_size) -> None: ...
    @property
    def first_item(self): ...
    @property
    def last_item(self): ...

class Page:
    collection: Incomplete
    page_params: Incomplete
    def __init__(self, collection, page_params) -> None: ...
    @property
    def items(self): ...
    @property
    def item_count(self): ...

class PaginationMetadataSchema(ma.Schema):
    total: Incomplete
    total_pages: Incomplete
    first_page: Incomplete
    last_page: Incomplete
    page: Incomplete
    previous_page: Incomplete
    next_page: Incomplete

PAGINATION_HEADER: Incomplete

class PaginationMixin:
    PAGINATION_ARGUMENTS_PARSER: Incomplete
    PAGINATION_HEADER_NAME: str
    DEFAULT_PAGINATION_PARAMETERS: Incomplete
    def paginate(
        self,
        pager: Incomplete | None = None,
        *,
        page: Incomplete | None = None,
        page_size: Incomplete | None = None,
        max_page_size: Incomplete | None = None,
    ): ...
