from _typeshed import Incomplete
from office365.onedrive.sensitivitylabels.assignment import SensitivityLabelAssignment as SensitivityLabelAssignment
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection

class ExtractSensitivityLabelsResult(ClientValue):
    labels: Incomplete
    def __init__(self, labels: Incomplete | None = None) -> None: ...
