from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class WikiPageCreationInformation(ClientValue):
    ServerRelativeUrl: Incomplete
    WikiHtmlContent: Incomplete
    def __init__(self, server_relative_url, content) -> None: ...
    @property
    def entity_type_name(self): ...
