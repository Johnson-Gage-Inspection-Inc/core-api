from _typeshed import Incomplete
from office365.outlook.geo_coordinates import (
    OutlookGeoCoordinates as OutlookGeoCoordinates,
)
from office365.outlook.mail.physical_address import PhysicalAddress as PhysicalAddress
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)

class Location(ClientValue):
    address: Incomplete
    coordinates: Incomplete
    displayName: Incomplete
    locationEmailAddress: Incomplete
    locationType: Incomplete
    locationUri: Incomplete
    uniqueId: Incomplete
    uniqueIdType: Incomplete
    def __init__(
        self,
        address=...,
        coordinates: Incomplete | None = None,
        display_name: Incomplete | None = None,
        location_email_address: Incomplete | None = None,
        location_type: Incomplete | None = None,
        location_uri: Incomplete | None = None,
        unique_id: Incomplete | None = None,
        unique_id_type: Incomplete | None = None,
    ) -> None: ...
