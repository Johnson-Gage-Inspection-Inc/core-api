from _typeshed import Incomplete
from office365.entity import Entity as Entity
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)

class WorkbookApplication(Entity):
    def calculate(self, calculation_type: Incomplete | None = None): ...
    @property
    def calculation_mode(self): ...
