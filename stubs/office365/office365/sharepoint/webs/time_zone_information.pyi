from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class TimeZoneInformation(ClientValue):
    Bias: Incomplete
    DaylightBias: Incomplete
    StandardBias: Incomplete
    def __init__(
        self,
        bias: Incomplete | None = None,
        standard_bias: Incomplete | None = None,
        daylight_bias: Incomplete | None = None,
    ) -> None: ...
