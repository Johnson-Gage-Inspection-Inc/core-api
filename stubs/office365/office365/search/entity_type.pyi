from office365.onedrive.driveitems.driveItem import DriveItem as DriveItem
from office365.onedrive.drives.drive import Drive as Drive
from office365.onedrive.listitems.list_item import ListItem as ListItem
from office365.onedrive.lists.list import List as List
from office365.onedrive.sites.site import Site as Site
from office365.outlook.calendar.events.event import Event as Event
from office365.outlook.mail.messages.message import Message as Message
from office365.outlook.person import Person as Person
from office365.search.external.item import ExternalItem as ExternalItem

class EntityType:
    def __init__(self) -> None: ...
    @staticmethod
    def resolve(
        name: str,
    ) -> type[Event | List | Site | ListItem | Message | Drive | DriveItem]: ...
    event: str
    list: str
    site: str
    listItem: str
    message: str
    drive: str
    driveItem: str
    externalItem: str
    person: str
