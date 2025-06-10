from _typeshed import Incomplete
from office365.directory.applications.app_identity import AppIdentity as AppIdentity
from office365.runtime.client_value import ClientValue as ClientValue

class AuditActivityInitiator(ClientValue):
    app: Incomplete
    user: Incomplete
    def __init__(self, app=..., user=...) -> None: ...
