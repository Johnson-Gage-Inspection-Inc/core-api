from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.types.collections import StringCollection as StringCollection

class WebApplication(ClientValue):
    homePageUrl: Incomplete
    logoutUrl: Incomplete
    redirectUris: Incomplete
    def __init__(
        self,
        home_page_url: Incomplete | None = None,
        logout_url: Incomplete | None = None,
        redirect_uris: Incomplete | None = None,
    ) -> None: ...
