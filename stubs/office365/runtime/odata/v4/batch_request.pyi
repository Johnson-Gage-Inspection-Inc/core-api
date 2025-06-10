from office365.runtime.http.http_method import HttpMethod as HttpMethod
from office365.runtime.http.request_options import RequestOptions as RequestOptions
from office365.runtime.odata.request import ODataRequest as ODataRequest
from office365.runtime.queries.batch import BatchQuery as BatchQuery
from office365.runtime.queries.client_query import ClientQuery as ClientQuery
from requests import Response

class ODataV4BatchRequest(ODataRequest):
    def build_request(self, query: BatchQuery) -> RequestOptions: ...
    def process_response(self, response: Response, query: BatchQuery) -> None: ...
