from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class FieldGeolocationValue(ClientValue):
    Latitude: Incomplete
    Longitude: Incomplete
    Altitude: Incomplete
    def __init__(
        self, latitude, longitude, altitude: Incomplete | None = None
    ) -> None: ...
    @property
    def entity_type_name(self): ...
