from _typeshed import Incomplete
from office365.outlook.calendar.attendees.availability import AttendeeAvailability as AttendeeAvailability
from office365.outlook.calendar.meetingtimes.time_slot import TimeSlot as TimeSlot
from office365.outlook.mail.location import Location as Location
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection

class MeetingTimeSuggestion(ClientValue):
    attendeeAvailability: Incomplete
    confidence: Incomplete
    locations: Incomplete
    meetingTimeSlot: Incomplete
    def __init__(self, attendee_availability: list[AttendeeAvailability] = None, confidence: float = None, locations: list[Location] = None, meeting_timeslot: TimeSlot = ...) -> None: ...
