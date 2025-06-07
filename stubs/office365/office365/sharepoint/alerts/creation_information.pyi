from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class AlertCreationInformation(ClientValue):
    AlertFrequency: Incomplete
    AlertTemplateName: Incomplete
    AlertType: Incomplete
    def __init__(self, alert_frequency, template_name, alert_type) -> None: ...
