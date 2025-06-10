from _typeshed import Incomplete
from office365.onenote.pages.external_link import ExternalLink as ExternalLink
from office365.runtime.client_value import ClientValue as ClientValue

class PageLinks(ClientValue):
    oneNoteClientUrl: Incomplete
    oneNoteWebUrl: Incomplete
    def __init__(self, onenote_client_url=..., onenote_web_url=...) -> None: ...
