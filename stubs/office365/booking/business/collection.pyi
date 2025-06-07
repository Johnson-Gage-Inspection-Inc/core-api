from _typeshed import Incomplete
from office365.booking.business.business import BookingBusiness as BookingBusiness
from office365.entity_collection import EntityCollection as EntityCollection
from office365.outlook.mail.physical_address import PhysicalAddress as PhysicalAddress

class BookingBusinessCollection(EntityCollection[BookingBusiness]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def add(self, display_name: str, address: PhysicalAddress | None = None, email: str | None = None) -> BookingBusiness: ...
