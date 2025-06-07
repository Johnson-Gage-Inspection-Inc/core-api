from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.sharepoint.apps.license import AppLicense as AppLicense

class AppLicenseCollection(ClientValue):
    Items: Incomplete
    def __init__(self, items=...) -> None: ...
