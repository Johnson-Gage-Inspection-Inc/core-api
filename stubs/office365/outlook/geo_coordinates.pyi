from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class OutlookGeoCoordinates(ClientValue):
    accuracy: Incomplete
    altitude: Incomplete
    altitudeAccuracy: Incomplete
    latitude: Incomplete
    longitude: Incomplete
    def __init__(
        self,
        accuracy: Incomplete | None = None,
        altitude: Incomplete | None = None,
        altitude_accuracy: Incomplete | None = None,
        latitude: Incomplete | None = None,
        longitude: Incomplete | None = None,
    ) -> None: ...
