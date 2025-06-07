import requests
from office365.runtime.client_object import ClientObject as ClientObject
from office365.runtime.client_request import ClientRequest as ClientRequest
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.http.http_method import HttpMethod as HttpMethod
from office365.runtime.http.request_options import RequestOptions as RequestOptions
from office365.runtime.odata.json_format import ODataJsonFormat as ODataJsonFormat
from office365.runtime.odata.v3.json_light_format import (
    JsonLightFormat as JsonLightFormat,
)
from office365.runtime.queries.client_query import ClientQuery as ClientQuery
from office365.runtime.queries.create_entity import (
    CreateEntityQuery as CreateEntityQuery,
)
from office365.runtime.queries.delete_entity import (
    DeleteEntityQuery as DeleteEntityQuery,
)
from office365.runtime.queries.function import FunctionQuery as FunctionQuery
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.runtime.queries.update_entity import (
    UpdateEntityQuery as UpdateEntityQuery,
)
from typing import Any

class ODataRequest(ClientRequest):
    def __init__(self, json_format: ODataJsonFormat) -> None: ...
    @property
    def json_format(self): ...
    def build_request(self, query: ClientQuery) -> RequestOptions: ...
    def process_response(
        self, response: requests.Response, query: ClientQuery
    ) -> None: ...
    def map_json(
        self,
        json: Any,
        return_type: ClientValue | ClientResult | ClientObject,
        json_format: ODataJsonFormat | None = None,
    ) -> None: ...
