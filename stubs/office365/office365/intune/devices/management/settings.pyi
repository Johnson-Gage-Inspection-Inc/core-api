from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class DeviceManagementSettings(ClientValue):
    deviceComplianceCheckinThresholdDays: Incomplete
    isScheduledActionEnabled: Incomplete
    secureByDefault: Incomplete
    def __init__(
        self,
        device_compliance_checkin_threshold_days: Incomplete | None = None,
        is_scheduled_action_enabled: Incomplete | None = None,
        secure_by_default: Incomplete | None = None,
    ) -> None: ...
