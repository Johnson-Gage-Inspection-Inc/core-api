from _typeshed import Incomplete
from office365.outlook.mail.location_constraint_item import LocationConstraintItem as LocationConstraintItem
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection

class LocationConstraint(ClientValue):
    isRequired: Incomplete
    locations: Incomplete
    suggestLocation: Incomplete
    def __init__(self, is_required: Incomplete | None = None, locations: Incomplete | None = None, suggest_location: Incomplete | None = None) -> None: ...
