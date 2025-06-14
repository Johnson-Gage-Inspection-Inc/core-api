from _typeshed import Incomplete
from flask import Blueprint as FlaskBlueprint

from .arguments import ArgumentsMixin as ArgumentsMixin
from .etag import EtagMixin as EtagMixin
from .pagination import PaginationMixin as PaginationMixin
from .response import ResponseMixin as ResponseMixin
from .utils import deepupdate as deepupdate
from .utils import load_info_from_docstring as load_info_from_docstring

class Blueprint(
    FlaskBlueprint, ArgumentsMixin, ResponseMixin, PaginationMixin, EtagMixin
):
    HTTP_METHODS: Incomplete
    DEFAULT_LOCATION_CONTENT_TYPE_MAPPING: Incomplete
    DOCSTRING_INFO_DELIMITER: str
    description: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def add_url_rule(
        self,
        rule,
        endpoint: Incomplete | None = None,
        view_func: Incomplete | None = None,
        provide_automatic_options: Incomplete | None = None,
        *,
        parameters: Incomplete | None = None,
        tags: Incomplete | None = None,
        **options,
    ) -> None: ...
    def route(
        self,
        rule,
        *,
        parameters: Incomplete | None = None,
        tags: Incomplete | None = None,
        **options,
    ): ...
    def register_blueprint(self, blueprint, **options): ...
    def register_views_in_doc(self, api, app, spec, *, name, parameters) -> None: ...
    @staticmethod
    def doc(**kwargs): ...
