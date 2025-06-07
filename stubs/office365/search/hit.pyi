from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class SearchHit(ClientValue):
    contentSource: Incomplete
    summary: Incomplete
    resource: Incomplete
    resultTemplateId: Incomplete
    def __init__(self, content_source: Incomplete | None = None, summary: Incomplete | None = None, resource: Incomplete | None = None, result_template_id: Incomplete | None = None) -> None: ...
