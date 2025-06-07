from _typeshed import Incomplete
from office365.onedrive.sites.archival_details import SiteArchivalDetails as SiteArchivalDetails
from office365.runtime.client_value import ClientValue as ClientValue

class SiteCollection(ClientValue):
    root: Incomplete
    hostname: Incomplete
    dataLocationCode: Incomplete
    archivalDetails: Incomplete
    def __init__(self, root: Incomplete | None = None, hostname: Incomplete | None = None, data_location_code: Incomplete | None = None, archival_details=...) -> None: ...
