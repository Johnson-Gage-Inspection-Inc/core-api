from _typeshed import Incomplete
from webargs.flaskparser import abort as abort

from .blueprint import Blueprint as Blueprint
from .error_handler import ErrorHandlerMixin
from .globals import current_api as current_api
from .pagination import Page as Page
from .spec import APISpecMixin

class Api(APISpecMixin, ErrorHandlerMixin):
    config_prefix: Incomplete
    config: Incomplete
    spec: Incomplete
    def __init__(
        self,
        app: Incomplete | None = None,
        *,
        spec_kwargs: Incomplete | None = None,
        config_prefix: str = "",
    ) -> None: ...
    def init_app(self, app, *, spec_kwargs: Incomplete | None = None) -> None: ...
    def register_blueprint(
        self, blp, *, parameters: Incomplete | None = None, **options
    ) -> None: ...
