from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class ParticipantInfo(ClientValue):
    countryCode: Incomplete
    def __init__(self, country_code: Incomplete | None = None) -> None: ...
