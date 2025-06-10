from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class DeviceDetail(ClientValue):
    browser: Incomplete
    deviceId: Incomplete
    displayName: Incomplete
    def __init__(
        self,
        browser: Incomplete | None = None,
        device_id: Incomplete | None = None,
        display_name: Incomplete | None = None,
    ) -> None: ...
