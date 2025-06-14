from typing import AnyStr

from office365.onenote.entity_base_model import (
    OnenoteEntityBaseModel as OnenoteEntityBaseModel,
)
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.queries.function import FunctionQuery as FunctionQuery

class OnenoteResource(OnenoteEntityBaseModel):
    def get_content(self) -> ClientResult[AnyStr]: ...
    @property
    def content_url(self) -> str | None: ...
