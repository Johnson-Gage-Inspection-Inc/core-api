from _typeshed import Incomplete
from office365.onedrive.driveitems.geo_coordinates import GeoCoordinates as GeoCoordinates
from office365.runtime.client_value import ClientValue as ClientValue

class SignInLocation(ClientValue):
    city: Incomplete
    countryOrRegion: Incomplete
    geoCoordinates: Incomplete
    state: Incomplete
    def __init__(self, city: Incomplete | None = None, country_or_region: Incomplete | None = None, geo_coordinates=..., state: Incomplete | None = None) -> None: ...
