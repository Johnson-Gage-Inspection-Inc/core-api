from _typeshed import Incomplete
from office365.delta_collection import DeltaCollection as DeltaCollection
from office365.outlook.calendar.email_address import EmailAddress as EmailAddress
from office365.outlook.contacts.contact import Contact as Contact
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.types.collections import StringCollection as StringCollection

class ContactCollection(DeltaCollection[Contact]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def add(
        self,
        given_name,
        surname,
        email_address: Incomplete | None = None,
        business_phone: Incomplete | None = None,
        **kwargs,
    ): ...
