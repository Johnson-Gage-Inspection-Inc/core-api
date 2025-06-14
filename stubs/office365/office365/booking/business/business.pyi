from datetime import datetime

from _typeshed import Incomplete
from office365.booking.appointment import BookingAppointment as BookingAppointment
from office365.booking.custom_question import (
    BookingCustomQuestion as BookingCustomQuestion,
)
from office365.booking.customers.base import BookingCustomerBase as BookingCustomerBase
from office365.booking.service import BookingService as BookingService
from office365.booking.staff.availability_item import (
    StaffAvailabilityItem as StaffAvailabilityItem,
)
from office365.booking.staff.member_base import (
    BookingStaffMemberBase as BookingStaffMemberBase,
)
from office365.booking.work_hours import BookingWorkHours as BookingWorkHours
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.outlook.mail.physical_address import PhysicalAddress as PhysicalAddress
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)

class BookingBusiness(Entity):
    def get_staff_availability(
        self,
        staff_ids: list[str] = None,
        start_datetime: datetime = None,
        end_datetime: datetime = None,
    ) -> ClientResult[ClientValueCollection[StaffAvailabilityItem]]: ...
    def publish(self): ...
    @property
    def address(self): ...
    @property
    def business_hours(self) -> ClientValueCollection[BookingWorkHours]: ...
    def display_name(self) -> str | None: ...
    @property
    def appointments(self) -> EntityCollection[BookingAppointment]: ...
    @property
    def calendar_view(self) -> EntityCollection[BookingAppointment]: ...
    @property
    def customers(self) -> EntityCollection[BookingCustomerBase]: ...
    @property
    def custom_questions(self): ...
    @property
    def services(self): ...
    @property
    def staff_members(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
