from _typeshed import Incomplete

class QueryOptions:
    select: Incomplete
    expand: Incomplete
    filter: Incomplete
    orderBy: Incomplete
    skip: Incomplete
    top: Incomplete
    custom: Incomplete
    def __init__(
        self,
        select: Incomplete | None = None,
        expand: Incomplete | None = None,
        filter_expr: Incomplete | None = None,
        order_by: Incomplete | None = None,
        top: Incomplete | None = None,
        skip: Incomplete | None = None,
        custom: Incomplete | None = None,
    ) -> None: ...
    @staticmethod
    def build(client_object, properties_to_include: Incomplete | None = None): ...
    @property
    def is_empty(self): ...
    def reset(self) -> None: ...
    def to_url(self): ...
    def __iter__(self): ...
