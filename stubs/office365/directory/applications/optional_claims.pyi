from _typeshed import Incomplete
from office365.directory.applications.optional_claim import OptionalClaim as OptionalClaim
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection

class OptionalClaims(ClientValue):
    accessToken: Incomplete
    idToken: Incomplete
    saml2Token: Incomplete
    def __init__(self, access_token: Incomplete | None = None, id_token: Incomplete | None = None, saml2_token: Incomplete | None = None) -> None: ...
