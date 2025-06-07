from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class SiteScriptMetadata(ClientValue):
    Id: Incomplete
    Content: Incomplete
    Description: Incomplete
    IsSiteScriptPackage: Incomplete
    Title: Incomplete
    Version: Incomplete
    def __init__(self, id_: Incomplete | None = None, content: Incomplete | None = None, description: Incomplete | None = None, is_site_script_package: Incomplete | None = None, title: Incomplete | None = None, version: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
