from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class GeoCoordinates(ClientValue):
    altitude: Incomplete
    latitude: Incomplete
    longitude: Incomplete
    def __init__(self, altitude: Incomplete | None = None, latitude: Incomplete | None = None, longitude: Incomplete | None = None) -> None: ...
