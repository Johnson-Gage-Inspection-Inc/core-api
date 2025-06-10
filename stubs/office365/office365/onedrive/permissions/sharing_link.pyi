from _typeshed import Incomplete
from office365.directory.permissions.identity import Identity as Identity
from office365.runtime.client_value import ClientValue as ClientValue

class SharingLink(ClientValue):
    type: Incomplete
    scope: Incomplete
    webHtml: Incomplete
    webUrl: Incomplete
    preventsDownload: Incomplete
    application: Incomplete
    def __init__(
        self,
        _type: Incomplete | None = None,
        scope: Incomplete | None = None,
        web_html: Incomplete | None = None,
        web_url: Incomplete | None = None,
        prevents_download: Incomplete | None = None,
        application=...,
    ) -> None: ...
