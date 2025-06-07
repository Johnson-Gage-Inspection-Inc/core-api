from _typeshed import Incomplete
from office365.delta_collection import DeltaCollection as DeltaCollection
from office365.intune.devices.alternative_security_id import AlternativeSecurityId as AlternativeSecurityId
from office365.intune.devices.device import Device as Device
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.runtime.queries.create_entity import CreateEntityQuery as CreateEntityQuery

class DeviceCollection(DeltaCollection[Device]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def add(self, display_name, operating_system, operating_system_version, account_enabled: bool = False, alternative_security_id: Incomplete | None = None, device_id: Incomplete | None = None): ...
