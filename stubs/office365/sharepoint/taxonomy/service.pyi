from office365.runtime.client_runtime_context import (
    ClientRuntimeContext as ClientRuntimeContext,
)
from office365.runtime.odata.request import ODataRequest as ODataRequest
from office365.runtime.odata.v4.json_format import V4JsonFormat as V4JsonFormat
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.sharepoint.taxonomy.stores.store import TermStore as TermStore

class TaxonomyService(ClientRuntimeContext):
    def __init__(self, context) -> None: ...
    def pending_request(self): ...
    def service_root_url(self): ...
    @property
    def term_store(self): ...
