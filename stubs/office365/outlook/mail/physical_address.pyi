from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class PhysicalAddress(ClientValue):
    city: Incomplete
    countryOrRegion: Incomplete
    postalCode: Incomplete
    state: Incomplete
    street: Incomplete
    def __init__(
        self,
        city: str | None = None,
        country_or_region: str | None = None,
        postal_code: str | None = None,
        state: str | None = None,
        street: str | None = None,
    ) -> None: ...
